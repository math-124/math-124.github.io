import unittest
from unittest.mock import Mock, patch
import update_recording as recording


class RecordingLoginTests(unittest.TestCase):
    def test_initial_recording_fetch_completes_login_before_scraping(self):
        context = Mock()
        page = context.new_page.return_value
        page.url = 'https://okta.umich.edu/signin'
        page.title.return_value = 'Recordings'
        nodes = Mock()
        nodes.count.return_value = 1
        row = nodes.nth.return_value
        row.locator.return_value.first.count.return_value = 1
        row.locator.return_value.first.get_attribute.return_value = '/leccap/player/r/Example'
        row.locator.return_value.count.return_value = 1
        row.locator.return_value.inner_text.return_value = 'October 13, 2026'

        def login(*args):
            page.url = recording.LECCAP_SITE_URL

        with patch.object(recording, '_ensure_logged_in', side_effect=login) as authenticate, \
                patch.object(recording, '_find_locator', return_value=(page, nodes)):
            result = recording._fetch_leccap_recordings_with_context(
                context, recording.LECCAP_SITE_URL, interactive_login=True)
        authenticate.assert_called_once_with(page, recording.LECCAP_SITE_URL, True)
        self.assertEqual(result[0]['href'], '/leccap/player/r/Example')


if __name__ == '__main__':
    unittest.main()
