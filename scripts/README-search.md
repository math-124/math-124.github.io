# Math 124 smart search

Course UI, ranking, the local model, and embedding tools are shared through `surajrampure/course-search`. The site loads its stable `/v1/` app and supplies `assets/course-search/config.json`. UI deployments update Math 124 and EECS 245 together.

The site deployment builds Jekyll, checks out the published notes and shared search tools, and runs `build_semantic_search.py`. It indexes only the published note TOC, linked homework/lab pages, released worksheets, and cached captions from published recordings. Homework due dates do not gate already published handouts. Future lecture entries are excluded.

Initial coverage is recordings 1–10, worksheets 6–10, 14 notes, homeworks 1–4, and labs 1–5. Lab 5 is a work session and links to its schedule entry. Practice exams are outside the requested categories.

Caption caches under `_data/lecture-transcripts` were captured read-only from the authenticated Chrome player's visible timestamped rows. `import_lecture_transcript.py` imports the captured row JSON into overlapping passages, with reviewed `--skip-before` and `--stop-after` bounds to exclude before/after-class chatter. Never commit credentials or raw browser session files. Builds use these caches offline and do not authenticate to Leccap. The generated metadata records source commits and caption-cache hashes.

Run the importer after Jekyll with Python packages from `search-requirements.txt`, passing `--notes` a clean public notes checkout and `--output` the shared checkout's `search-index.json`. Run `npm run embed` there; copy its `public/data` to `_site/assets/course-search/data`. The workflow automates these steps. To add recordings later, acquire authentic timed captions, review their class boundaries, import and commit the new cache, then rebuild.
