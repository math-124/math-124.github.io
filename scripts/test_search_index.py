"""Regression checks for published note visibility and optional TOC titles."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml
from build_search_index import published_notes


class PublishedNotesTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.notes = Path(self.directory.name)
        self.fetch = patch("build_search_index.urlopen").start()
        self.addCleanup(patch.stopall)
        self.fetch.return_value.read.return_value = b'<article><h2 id="example">Example</h2></article>'

    def write_toc(self, toc):
        (self.notes / "myst.yml").write_text(yaml.safe_dump({"project": {"toc": toc}}))

    def write_note(self, source):
        path = self.notes / "ch03/03-01.ipynb"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"cells": [{"cell_type": "markdown", "source": source}]}))
        return "ch03/03-01.ipynb"

    def test_hidden_entries_and_their_children_are_skipped(self):
        self.write_toc([
            {"file": "ch03/missing.ipynb", "hidden": True},
            {"title": "Hidden chapter", "hidden": True,
             "children": [{"file": "ch03/also-missing.ipynb"}]},
        ])
        self.assertEqual(published_notes(self.notes), [])
        self.fetch.assert_not_called()

    def test_missing_title_uses_notebook_heading(self):
        file = self.write_note(["---\n\n# 3.1: Matrices\n", "An introduction.\n"])
        self.write_toc([{"file": file}])
        document, = published_notes(self.notes)
        self.assertEqual(document["title"], "3.1: Matrices")
        self.assertEqual(document["passages"][0]["label"], "3.1: Matrices")
        self.assertIn("An introduction.", document["passages"][0]["text"])

    def test_missing_heading_uses_filename(self):
        file = self.write_note(["An introduction.\n"])
        self.write_toc([{"file": file, "title": ""}])
        document, = published_notes(self.notes)
        self.assertEqual(document["title"], "03-01")

    def test_explicit_title_and_section_anchors_are_preserved(self):
        file = self.write_note(["# Notebook heading\nIntroduction.\n", "## Example\nSome content.\n"])
        (self.notes / file).write_text(json.dumps({"cells": [
            {"cell_type": "markdown", "source": ["# Notebook heading\nIntroduction.\n"]},
            {"cell_type": "markdown", "source": ["## Example\nSome content.\n"]},
        ]}))
        self.write_toc([{"title": "Chapter", "children": [{"file": file, "title": "TOC title"}]}])
        document, = published_notes(self.notes)
        self.assertEqual(document["title"], "TOC title")
        self.assertEqual(document["passages"][1]["url"], document["url"] + "#example")


if __name__ == "__main__":
    unittest.main()
