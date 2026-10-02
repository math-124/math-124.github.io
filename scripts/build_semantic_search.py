#!/usr/bin/env python3
"""Adapt Math 124's released materials to the shared semantic-search schema."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path
from build_search_index import build


def convert(data, output):
    records = []
    for doc in data["documents"]:
        for passage in doc["passages"]:
            category = {"notes":"Notes", "homeworks":"Homeworks", "labs":"Labs", "lectures":"Lecture PDFs"}[doc["type"]]
            url = passage["url"]
            if url.startswith('/'):
                url = 'https://math124.org' + url
            text = passage["text"]
            section = passage["label"]
            extra = {}
            if doc["type"] == 'lectures':
                if section.startswith('Recording · '):
                    category = 'Lecture recordings'
                    parts = section.split(' · ')[1].split(':')
                    start = int(parts[0])*60 + int(parts[1])
                    extra = {"start":start, "end":passage.get('end',start+45), "recordingUrl":url,
                             "lectureDate":doc['date'], "recordingId":url.rsplit('/',1)[-1]}
                    url += '?start=' + str(max(0,start-5))
                    section = section.split(' · ')[1]
                elif section.startswith('Worksheet'):
                    section = 'Page ' + section.rsplit(' ',1)[-1]
                else:
                    # The semantic lecture corpus uses recordings and worksheets.
                    continue
            tags = [name for name, pattern in [
                ('dot product',r'dot product|cosine similarity|inner product'),
                ('projection',r'project(?:ion|ions|ing)?'),
                ('orthogonal',r'orthogonal|perpendicular'),
                ('span',r'\bspan\b|linear combination'),
                ('normal vector',r'normal vector'),
                ('basis',r'basis|bases|orthonormal'),
            ] if re.search(pattern,text,re.I)]
            records.append({"id":str(len(records)),"category":category,"title":doc["title"],
                            "section":section,"text":text,"url":url,"detail":"Lecture captions" if category=='Lecture recordings' else "Published course material",
                            "concepts":tags,"releaseAt":doc.get('release',doc.get('date','2026-08-01'))+'T00:00:00-04:00',"semester":"Fall 2026",**extra})
    payload={"records":records,"metadata":{"builtAt":dt.datetime.now(dt.timezone.utc).isoformat(),
             "errors":[],"course":"Math 124","coverage":data['counts'],"sources":data['sources'],
             "recordings":{"published":data['recordings'],"available":data['transcribed']}}}
    output.write_text(json.dumps(payload,ensure_ascii=False))
    print(f"Math 124: {len(records)} source passages for semantic search")


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notes',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    site=Path(__file__).resolve().parents[1]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    convert(build(site,args.notes,site/'_site/assets/search-index.json'),args.output)
