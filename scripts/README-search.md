# Math 124 smart search

Course UI, ranking, the local model, and embedding tools are shared through `surajrampure/course-search`. The site loads its stable `/v1/` app and supplies `assets/course-search/config.json`. UI deployments update Math 124 immediately; EECS 245 will share these updates after its pending migration.

The site deployment builds Jekyll, checks out the published notes and shared search tools, and runs `build_semantic_search.py`. It indexes only the published note TOC, linked homework/lab pages, released worksheets, and cached captions from published recordings. Homework due dates do not gate already published handouts. Future lecture entries are excluded.

Initial coverage is recordings 1–10, worksheets 6–10, 14 notes, homeworks 1–4, and labs 1–5. Lab 5 is a work session and links to its schedule entry. Practice Midterm 1 is indexed as an exam, with links to all seven problems.

Caption caches under `_data/lecture-transcripts` were captured read-only from the authenticated Chrome player's visible timestamped rows. `import_lecture_transcript.py` imports the captured row JSON into overlapping passages, with reviewed `--skip-before` and `--stop-after` bounds to exclude before/after-class chatter. Never commit credentials or raw browser session files. Builds use these caches offline and do not authenticate to Leccap. The generated metadata records source commits and caption-cache hashes.

Run the importer after Jekyll with Python packages from `search-requirements.txt`, passing `--notes` a clean public notes checkout and `--output` the shared checkout's `search-index.json`. Run `npm run embed` there; copy its `public/data` to `_site/assets/course-search/data`. The workflow automates these steps. To add recordings later, acquire authentic timed captions, review their class boundaries, import and commit the new cache, then rebuild.

Practice exams linked from the homepage or Resources page are indexed by problem, including published solutions. The Math 124 interface calls lecture PDFs “Lecture worksheets” and past exams “Exams”.

“Other videos” indexes only the titles and direct video links in `_data/other-videos.json`: the six reviewed videos from Kartik's “Linear Algebra, Visually” playlist and the standalone plane-equation video on Resources. Builds use this fixed list without fetching YouTube or indexing transcripts. Edit the list explicitly to change the searchable videos.

### Separate recording and caption buttons

The **124 Recording** Apple Shortcut runs `scripts/update_recording.py --recording-only --interactive-login`. It publishes the latest recording link and updates the selected CAEN recording titles. It never requests captions, so caption availability and caption download errors cannot block recording publication. `--title-count N` selects the number of recording titles to update.

The **124 Captions & Search** Apple Shortcut runs `scripts/update_recording.py --refresh-captions --interactive-login`. It downloads current WebVTT captions for all released lectures that already have recording links. It does not edit links or titles. Confirmed CAEN processing notices are reported and skipped; malformed or unauthenticated responses fail without replacing an existing cache. Existing reviewed lecture bounds are preserved; new caches use the complete available caption track.

The caption button commits only caption caches and triggers the existing website build, which rebuilds the full search index and semantic embeddings. An unchanged refresh still triggers a rebuild so it can repair a failed or stale index. Wait for the website deployment to finish before expecting new captions in public search. Builds remain offline with respect to Leccap; no browser session or credentials are committed.
