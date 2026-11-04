#!/usr/bin/env python3
"""Publish only the Lab 10 homepage link on November 4, 2026, at 5 PM Eastern."""
from datetime import datetime, timezone
from pathlib import Path
import subprocess

START = datetime(2026, 11, 4, 22, tzinfo=timezone.utc)
END = datetime(2026, 11, 5, 5, tzinfo=timezone.utc)
OLD = "        title: Column Space\n"
NEW = OLD + "        problems: ../resources/labs/lab10/\n        solutions: true\n"


def add_link(text):
    start = text.index("      - name: LAB 10\n")
    end = text.index('  - date: "2026-11-05"', start)
    block = text[start:end]
    if NEW in block:
        return text
    if block.count(OLD) != 1 or "problems:" in block or "solutions:" in block:
        raise ValueError("Lab 10 homepage entry changed; refusing to overwrite it")
    return text[:start] + block.replace(OLD, NEW) + text[end:]


def main():
    if not START <= datetime.now(timezone.utc) < END:
        raise SystemExit("Outside the authorized November 4 release window")
    path = Path("_modules/week-10.md")
    original = path.read_text()
    updated = add_link(original)
    if updated == original:
        print("Lab 10 is already linked")
        return
    path.write_text(updated)
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
    subprocess.run(["git", "add", str(path)], check=True)
    subprocess.run(["git", "commit", "-m", "Publish Lab 10 homepage link"], check=True)
    subprocess.run(["git", "push", "origin", "HEAD:main"], check=True)


if __name__ == "__main__":
    main()
