#!/usr/bin/env python3
"""Index released course resources. Run after Jekyll; never crawl private materials."""
import argparse
import datetime as dt
import json
import hashlib
import subprocess
import re
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen
from zoneinfo import ZoneInfo

import yaml
from bs4 import BeautifulSoup
from pypdf import PdfReader


def clean(value):
    value = re.sub(r"^---\s*\n.*?\n---\s*\n", "", str(value), flags=re.S)
    value = re.sub(r"^\s*(?:::[^\n]*|:[\w-]+:[^\n]*|```[^\n]*)$", " ", value, flags=re.M)
    value = re.sub(r"^\s*---\s*$", " ", value, flags=re.M)
    value = re.sub(r"\\begin\{bmatrix\}(.*?)\\end\{bmatrix\}",
                   lambda match: "(" + match[1].replace("\\\\", ", ") + ")", value, flags=re.S)
    value = re.sub(r"\\mathbb\s*\{?R\}?\s*\^\s*\{?([23])\}?",
                   lambda match: "ℝ" + {"2": "²", "3": "³"}[match[1]], value)
    value = re.sub(r"\\(?:vec|left|right|quad|qquad|displaystyle)\b|\\[()]|\*\*|__", "", value)
    value = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", str(value), flags=re.S)
    value = BeautifulSoup(value, "html.parser").get_text(" ")
    value = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\\(?:begin|end)\{[^}]*\}|\\(?:label|tag)\{[^}]*\}", " ", value)
    value = re.sub(r"\\(?:mathbf|mathrm|mathbb|text|operatorname)\{([^}]*)\}", r"\1", value)
    value = re.sub(r"\\([a-zA-Z]+)", r" \1 ", value)
    return re.sub(r"\s+", " ", re.sub(r"[{}$`#]", " ", value)).strip()


def metadata(path):
    return yaml.safe_load(path.read_text().split("---", 2)[1])


def pdf_passages(path, url, label):
    return [{"text": clean(page.extract_text() or ""), "url": f"{url}#page={i}",
             "label": f"{label}, page {i}"}
            for i, page in enumerate(PdfReader(path).pages, 1)]


def html_passages(path, url):
    soup = BeautifulSoup(path.read_text(), "html.parser")
    main = soup.select_one("#main-content main") or soup.select_one("main.main-content") or soup.select_one("#main-content")
    if main is None:
        raise ValueError(f"No main content in {path}")
    # These are presentation controls; retain only the published problem text.
    for node in main.select("script, style, svg, .assignment-actions, .anchor-heading"):
        node.decompose()
    passages, text, label, anchor = [], [], "Problems", ""
    for node in main.children:
        if getattr(node, "name", None) in ("h2", "h3"):
            if text:
                passages.append({"text": clean(" ".join(text)), "label": label, "url": url + anchor})
            label, anchor, text = clean(node.get_text(" ")), "#" + node.get("id", ""), []
        text.append(node.get_text(" ") if hasattr(node, "get_text") else str(node))
    if text:
        passages.append({"text": clean(" ".join(text)), "label": label, "url": url + anchor})
    return [p for p in passages if p["text"] and (len(passages) == 1 or p["label"] not in ("Problems", "Activities"))]


def published_notes(notes):
    toc = yaml.safe_load((notes / "myst.yml").read_text())["project"]["toc"]
    def walk(items):
        for item in items:
            if item.get("hidden"):
                continue
            if item.get("file", "").startswith("ch"):
                path = notes / item["file"]
                url = "https://notes.math124.org/" + str(Path(item["file"]).with_suffix("")) + "/"
                cells = json.loads(path.read_text())["cells"]
                title = item.get("title")
                if not title:
                    for cell in cells:
                        if cell["cell_type"] == "markdown":
                            heading = re.search(r"^#\s+(.+)", "".join(cell["source"]), re.M)
                            if heading:
                                title = clean(heading[1])
                                break
                title = title or path.stem
                rendered = BeautifulSoup(urlopen(url,timeout=30).read(), 'html.parser')
                anchors = {clean(h.get_text(' ',strip=True).replace('¶','')): h.get('id')
                           for h in rendered.select('article h2, article h3, article h4') if h.get('id')}
                passages, label = [], title
                section_url = url
                for cell in cells:
                    if cell["cell_type"] != "markdown":
                        continue
                    source = "".join(cell["source"])
                    heading = re.search(r"^#{1,4}\s+(.+)", source, re.M)
                    if heading:
                        label = clean(heading[1])
                        section_url = url + '#' + anchors[label] if label in anchors else url
                    text = clean(source)
                    if text and text != label:
                        passages.append({"text": text, "label": label, "url": section_url})
                yield {"id": "note-" + path.stem, "type": "notes", "title": title,
                       "url": url, "links": [{"label": "Read note", "url": url}], "passages": passages}
            yield from walk(item.get("children", []))
    return list(walk(toc))


def build(site, notes, output):
    documents = published_notes(notes)
    note_lookup = {d["url"].rstrip("/"): d for d in documents}
    home = BeautifulSoup((site / "_site/index.html").read_text(), "html.parser")
    weeks = {int(p.name.split("-")[1].split(".")[0]): metadata(p)
             for p in sorted((site / "_modules").glob("*.md"))}
    week_anchors = [h.get("id") for h in home.select(".module-header")]
    recordings, transcribed = 0, 0
    for (week_number, week), anchor in zip(weeks.items(), week_anchors):
        for day in week.get("days", []):
            for event in day.get("events", []):
                kind = event.get("type")
                if kind not in ("lecture", "lab", "hw"):
                    continue
                if kind != 'hw' and dt.date.fromisoformat(str(day['date'])) > dt.datetime.now(ZoneInfo('America/Detroit')).date():
                    continue
                number = re.search(r"\d+", event["name"])[0]
                title = clean(event.get("title", event["name"]))
                name = {"lecture": "Lecture", "lab": "Lab", "hw": "Homework"}[kind]
                links, passages = [], []
                resource = event.get("problems")
                if kind != "lecture" and not resource:
                    # A released work-session lab still belongs in search.
                    if kind != "lab" or not any(x in title.lower() for x in ("session", "review")):
                        continue
                if resource:
                    url = urljoin("https://math124.org/", resource).removeprefix("https://math124.org")
                    path = site / "_site" / url.lstrip("/") / "index.html"
                    if not path.exists():
                        raise FileNotFoundError(path)
                    links.append({"label": "Problems", "url": url})
                    passages += html_passages(path, url)
                else:
                    url = "/#" + anchor
                if kind == "lecture":
                    for key, value in event.items():
                        if key.startswith("recording") and value:
                            links.append({"label": "Recording" if key == "recording" else key.title(), "url": value})
                    if not links and not event.get("worksheet"):
                        continue
                    if event.get("recording"):
                        recordings += 1
                    if event.get("worksheet"):
                        worksheet = urljoin("https://math124.org/", event["worksheet"]).removeprefix("https://math124.org")
                        links.append({"label": "Worksheet", "url": worksheet})
                        passages += pdf_passages(site / worksheet.lstrip("/"), worksheet, "Worksheet")
                    # Notes supply accurate topic terms until captions are available.
                    for key, value in event.items():
                        if re.fullmatch(r"reading\d*", key) and value:
                            note = note_lookup.get(value.rstrip("/"))
                            if note:
                                passages.append({"text": note["title"], "label": "Assigned reading", "url": url})
                    transcript = site / "_data/lecture-transcripts" / f"lec{int(number):02d}.json"
                    if transcript.exists():
                        captions = json.loads(transcript.read_text())
                        if captions["recording"] != event.get("recording"):
                            raise ValueError(f"Recording mismatch in {transcript}")
                        for cue in captions["segments"]:
                            seconds = int(cue["start"])
                            passages.append({"text": clean(cue["text"]),
                                             "label": f"Recording · {seconds // 60}:{seconds % 60:02d}",
                                             "url": cue.get("url", event["recording"]), "start":seconds,
                                             "end":cue.get("end",seconds+45)})
                        transcribed += 1
                if not passages:
                    passages.append({"text": title, "label": day["date"], "url": url})
                release = day['date']
                if kind == 'hw':
                    # Homework schedule dates are deadlines, not publication dates.
                    source = url.split('#')[0].strip('/') + '/index.md'
                    dates = subprocess.check_output(['git','-C',str(site),'log','--reverse','--format=%cI','--',source],text=True).splitlines()
                    if not dates:
                        raise ValueError(f'No public source history for {source}')
                    release = dates[0][:10]
                documents.append({"id": f"{kind}-{number}", "type": {"lecture": "lectures", "lab": "labs", "hw": "homeworks"}[kind],
                                  "title": f"{name} {number}: {title}", "url": url, "date": day["date"], "release":release,
                                  "links": links, "passages": passages})
    # Only exam pages linked from the published site enter the corpus.
    linked = {urljoin("https://math124.org/", a["href"]).split("#")[0].split("?")[0].rstrip("/")
              for page in (site / "_site/index.html", site / "_site/resources/index.html") if page.exists()
              for a in BeautifulSoup(page.read_text(), "html.parser").select("a[href]")}
    for source in sorted((site / "resources/exams").glob("*/index.md")):
        url = "/" + str(source.parent.relative_to(site)) + "/"
        if ("https://math124.org" + url).rstrip("/") not in linked:
            continue
        dates = subprocess.check_output(["git", "-C", str(site), "log", "--reverse", "--format=%cI", "--", str(source.relative_to(site))], text=True).splitlines()
        if not dates:
            raise ValueError(f"No public source history for {source}")
        documents.append({"id": "exam-" + source.parent.name, "type": "exams", "title": metadata(source)["title"],
                          "url": url, "release": dates[0][:10], "date": dates[0][:10],
                          "links": [{"label": "Problems", "url": url}],
                          "passages": html_passages(site / "_site" / url.lstrip("/") / "index.html", url)})
    # A reviewed fixed list, indexed by title without fetching YouTube at build time.
    videos = json.loads((site / "_data/other-videos.json").read_text())
    for number, video in enumerate(videos, 1):
        title, url = video["title"], video["url"]
        documents.append({"id": f"other-video-{number}", "type": "other-videos",
                          "title": title, "url": url,
                          "links": [{"label": "Watch video", "url": url}],
                          "passages": [{"text": title, "label": "Watch video", "url": url}]})
    counts = {kind: sum(d["type"] == kind for d in documents) for kind in ("lectures", "notes", "homeworks", "labs", "exams", "other-videos")}
    payload = {"version": 1, "counts": counts, "recordings": recordings,
               "transcribed": transcribed, "documents": documents,
               "sources": {"websiteCommit":subprocess.check_output(['git','-C',str(site),'rev-parse','HEAD'],text=True).strip(),
                           "notesCommit":subprocess.check_output(['git','-C',str(notes),'rev-parse','HEAD'],text=True).strip(),
                           "otherVideos":hashlib.sha256((site/'_data/other-videos.json').read_bytes()).hexdigest(),
                           "transcripts":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((site/'_data/lecture-transcripts').glob('*.json'))}}}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(json.dumps({**counts, "transcribed": transcribed, "bytes": output.stat().st_size}))
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--notes", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    build(args.site, args.notes, args.output or args.site / "_site/assets/search-index.json")
