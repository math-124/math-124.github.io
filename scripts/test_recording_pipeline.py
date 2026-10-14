import tempfile
from pathlib import Path
import unittest
from unittest.mock import Mock, MagicMock, patch

import update_recording as recording


class PipelineTests(unittest.TestCase):
    def test_recording_publication_never_requests_captions(self):
        browser, context = Mock(), Mock()
        target = dict(module_path='/schedule', date_str='2026-10-13',
                      date_obj=None, recording_url='https://example.com/recording',
                      lecture_number='13', lecture_name='LEC 13',
                      lecture_title='Composition', recording_title='Lecture 13')
        with patch('sys.argv', ['update_recording.py', '--recording-only', '--interactive-login']), \
                patch('playwright.sync_api.sync_playwright', return_value=MagicMock()), \
                patch.object(recording, 'synchronize_git'), \
                patch.object(recording, '_launch_browser', return_value=browser), \
                patch.object(recording, '_create_context', return_value=context), \
                patch.object(recording, '_fetch_leccap_recordings_with_context', return_value=[{}]), \
                patch.object(recording, 'build_recording_target', return_value=target), \
                patch.object(recording, 'select_recent_recordings', return_value=[{}]), \
                patch.object(recording, 'update_recording'), \
                patch.object(recording, 'update_recording_title'), \
                patch.object(recording, 'run_git_commands') as publish, \
                patch('recording_captions.refresh_captions', side_effect=RuntimeError('caption server failed')) as captions:
            recording.main()
        captions.assert_not_called()
        publish.assert_called_once_with('/schedule', 'LEC 13', 'https://example.com/recording')
        browser.close.assert_called_once()

    def test_caption_mode_never_edits_recording_links_or_titles(self):
        context = Mock()
        with patch('sys.argv', ['update_recording.py', '--refresh-captions', '--interactive-login']), \
                patch('playwright.sync_api.sync_playwright', return_value=MagicMock()), \
                patch.object(recording, 'synchronize_git'), \
                patch.object(recording, '_launch_browser'), \
                patch.object(recording, '_create_context', return_value=context), \
                patch.object(recording, 'refresh_published_captions') as refresh, \
                patch.object(recording, '_fetch_leccap_recordings_with_context') as fetch, \
                patch.object(recording, 'update_recording') as link, \
                patch.object(recording, 'update_recording_title') as title:
            recording.main()
        refresh.assert_called_once_with(context, True)
        fetch.assert_not_called()
        link.assert_not_called()
        title.assert_not_called()

    def test_caption_targets_exclude_unlinked_future_and_nonlecture_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, 'week-01.md').write_text('''---
days:
  - date: "2000-01-01"
    events:
      - {name: LEC 1, type: lecture, recording: "https://example.com/one"}
      - {name: LEC 2, type: lecture}
      - {name: LAB 1, type: lab, recording: "https://example.com/lab"}
  - date: "2999-01-01"
    events:
      - {name: LEC 3, type: lecture, recording: "https://example.com/future"}
---
''')
            with patch.object(recording, 'MODULES_DIR', tmp):
                targets = recording.published_recording_targets()
        self.assertEqual([t['lecture_number'] for t in targets], ['1'])
        self.assertEqual(targets[0]['recording_url'], 'https://example.com/one')


if __name__ == '__main__':
    unittest.main()
