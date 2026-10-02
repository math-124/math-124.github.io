#!/usr/bin/env python3
"""Import timestamped transcript rows exported from the lecture player's visible UI."""
import argparse
import json
import re
from pathlib import Path


def seconds(timestamp):
    total = 0
    for part in timestamp.split(":"):
        total = total * 60 + int(part)
    return total


def convert(source, output, skip_before=0, stop_after=None):
    raw = json.loads(source.read_text())
    rows = [{"start": seconds(row["time"]), "text": re.sub(r"\s+", " ", row["text"]).strip()}
            for row in raw["rows"] if seconds(row["time"]) >= skip_before and (stop_after is None or seconds(row["time"]) <= stop_after)]
    if not rows or any(b["start"] < a["start"] for a, b in zip(rows, rows[1:])):
        raise ValueError("Transcript must contain rows in chronological order")
    # A 45-second window with overlap preserves context across caption boundaries.
    segments = []
    i = 0
    while i < len(rows):
        start = rows[i]["start"]
        j = i
        while j < len(rows) and rows[j]["start"] < start + 45:
            j += 1
        segments.append({"start": start, "end":rows[j-1]['start'], "text": " ".join(row["text"] for row in rows[i:j])})
        next_i = i + 1
        while next_i < j and rows[next_i]["start"] < start + 35:
            next_i += 1
        i = next_i
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"recording": raw["recording"].split('?')[0], "source": "CAEN lecture viewer transcript",
                                  "lectureRange": {"start":skip_before, "end":stop_after},
                                  "segments": segments}, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"{output.name}: {len(rows)} caption rows, {len(segments)} passages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--skip-before", type=int, default=0)
    parser.add_argument("--stop-after", type=int)
    args = parser.parse_args()
    convert(args.source, args.output, args.skip_before, args.stop_after)
