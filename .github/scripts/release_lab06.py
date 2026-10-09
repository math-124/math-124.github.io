"""One-time, pinned Lab 6 publication; run from the website repository root."""
import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import runpy
import subprocess
import tempfile
import time
import urllib.request

PAYLOAD = "e7728bf7e618001f0135da96332b781eafb699af"
RESOURCE = "resources/labs/lab06"
MODULE = "_modules/week-06.md"
START = datetime(2026, 10, 7, 21, tzinfo=timezone.utc)
END = datetime(2026, 10, 8, 1, tzinfo=timezone.utc)


def git(*args, **kwargs):
    return subprocess.check_output(["git", *args], **kwargs)


def payload():
    git("fetch", "origin", "scheduled/lab06-2026-10-07")
    names = git("ls-tree", "-r", "--name-only", PAYLOAD, RESOURCE).decode().splitlines()
    expected = {
        f"{RESOURCE}/index.md", f"{RESOURCE}/lab06.pdf",
        f"{RESOURCE}/lab06-solutions.pdf", f"{RESOURCE}/imgs/lab06-plot-01.png",
        f"{RESOURCE}/imgs/lab06-plot-02.png",
    }
    assert set(names) == expected, names
    return {name: git("show", f"{PAYLOAD}:{name}") for name in names}


def linked_module(text):
    pattern = r'(      - name: LAB 6\n)(.*?)(?=  - date:|\n---|\Z)'
    matches = list(re.finditer(pattern, text, re.S))
    assert len(matches) == 1, "Expected exactly one LAB 6 event"
    match = matches[0]
    body = match.group(2)
    assert 'title: "Matrix-Vector Multiplication"' in body
    body = re.sub(r'^        (?:colab_link|problems|solutions|note):.*\n', '', body, flags=re.M)
    body += f'        problems: ../{RESOURCE}/\n'
    return text[:match.start()] + match.group(1) + body + text[match.end():]


def validate(files):
    page = files[f"{RESOURCE}/index.md"].decode()
    assert page.count('<summary>Solution</summary>') >= 10
    for filename in ('lab06.pdf', 'lab06-solutions.pdf'):
        assert f'/{RESOURCE}/{filename}' in page
        assert files[f'{RESOURCE}/{filename}'].startswith(b'%PDF-')
    for img in re.findall(r'<img[^>]+src="(imgs/[^\"]+)"', page):
        assert f'{RESOURCE}/{img}' in files
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory) / 'lab06'
        for name, data in files.items():
            path = target / Path(name).relative_to(RESOURCE)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        checker = runpy.run_path('scripts/check_assignment_html.py')
        failures = checker['check_source_markdown'](target / 'index.md', allow_solutions=True)
        assert not failures, failures
    linked_module(Path(MODULE).read_text())
    print('Validated worksheet, solutions, web view, diagram assets, and homepage event.', flush=True)


def prepare(files):
    for name, data in files.items():
        path = Path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    path = Path(MODULE)
    path.write_text(linked_module(path.read_text()))
    git('diff', '--check')


def verify_live(files):
    deadline = time.time() + 1200
    last_error = None
    while time.time() < deadline:
        try:
            for name, expected in files.items():
                if name.endswith('index.md'):
                    continue
                with urllib.request.urlopen(f'https://math124.org/{name}?release={PAYLOAD}', timeout=30) as response:
                    assert hashlib.sha256(response.read()).digest() == hashlib.sha256(expected).digest(), name
            with urllib.request.urlopen(f'https://math124.org/{RESOURCE}/?release={PAYLOAD}', timeout=30) as response:
                page = response.read().decode()
                assert 'Solution</summary>' in page and 'lab06-solutions.pdf' in page
            with urllib.request.urlopen(f'https://math124.org/?release={PAYLOAD}', timeout=30) as response:
                home = response.read().decode()
                assert re.search(r'<a\s+href="(?:\.\./|/)?resources/labs/lab06/"[^>]*>\s*Matrix-Vector Multiplication\s*</a>', home)
                assert 'https://colab.research.google.com/github/math-124/fa26-code/blob/main/labs/lab06/lab06.ipynb' not in home
            print('Verified live homepage, solution dropdowns, both PDFs, and both diagram assets.', flush=True)
            return
        except Exception as error:
            last_error = error
            time.sleep(30)
    raise RuntimeError(f'Live verification did not pass: {last_error}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['validate', 'prepare', 'publish', 'verify'])
    args = parser.parse_args()
    files = payload()
    validate(files)
    if args.mode == 'validate':
        return
    if args.mode == 'verify':
        verify_live(files)
        return
    if args.mode == 'prepare':
        prepare(files)
        return
    assert START <= datetime.now(timezone.utc) < END, 'Outside the authorized release window'
    assert not git('status', '--porcelain').strip(), 'Publishing checkout must be clean'
    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    for attempt in range(3):
        git('fetch', 'origin', 'main')
        git('checkout', '-B', 'lab06-publication', 'origin/main')
        prepare(files)
        git('add', MODULE, RESOURCE)
        if git('diff', '--cached', '--name-only').strip():
            git('commit', '-m', 'Publish Lab 6 worksheet, solutions, and web view')
        result = subprocess.run(['git', 'push', 'origin', 'HEAD:main'])
        if result.returncode == 0:
            break
        if attempt == 2:
            raise RuntimeError('Publication push failed after three attempts')
    print('Published commit ' + git('rev-parse', 'HEAD').decode().strip(), flush=True)


if __name__ == '__main__':
    main()
