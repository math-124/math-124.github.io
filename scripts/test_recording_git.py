"""Exercise recording publication against real disposable Git repositories."""
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('recording', Path(__file__).with_name('update_recording.py'))
recording = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recording)


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.STDOUT, text=True)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.remote = root / 'remote.git'
        subprocess.check_call(['git', 'init', '--bare', '--initial-branch=main', '-q', str(self.remote)])
        git(self.remote, 'config', 'uploadpack.allowFilter', 'true')
        self.local = root / 'local'
        self.other = root / 'other'
        git(root, 'clone', self.remote.as_uri(), str(self.local))
        for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
            git(self.local, 'config', key, value)
        (self.local / 'schedule').write_text('lecture\n')
        (self.local / 'unrelated').write_text('original\n')
        git(self.local, 'add', '.')
        git(self.local, 'commit', '-m', 'Initial')
        git(self.local, 'push', '-u', 'origin', 'HEAD')
        git(root, 'clone', self.remote.as_uri(), str(self.other))
        for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
            git(self.other, 'config', key, value)

    def remote_change(self, filename, text):
        (self.other / filename).write_text(text)
        git(self.other, 'add', filename)
        git(self.other, 'commit', '-m', 'Remote update')
        git(self.other, 'push')

    def test_publish_ignores_desktop_drafts_and_rebases_on_new_releases(self):
        (self.local / 'unrelated').write_text('staged draft\n')
        git(self.local, 'add', 'unrelated')
        (self.local / 'unrelated').write_text('staged and unstaged drafts\n')
        (self.local / 'released').write_text('untracked draft\n')
        (self.local / 'schedule').write_text('schedule draft\n')
        head = git(self.local, 'rev-parse', 'HEAD')
        staged = git(self.local, 'diff', '--cached')
        unstaged = git(self.local, 'diff')
        self.remote_change('unrelated', 'overlapping release\n')
        self.remote_change('released', 'published version\n')

        with recording.publication_checkout(self.local) as checkout:
            self.assertEqual(git(checkout, 'rev-parse', '--is-shallow-repository').strip(), 'true')
            self.assertEqual((checkout / 'schedule').read_text(), 'lecture\n')
            (checkout / 'schedule').write_text('lecture\nrecording\n')
            self.remote_change('another-release', 'newer release\n')
            with contextlib.redirect_stdout(io.StringIO()):
                recording.run_git_commands(
                    checkout, checkout / 'schedule', 'LEC 12', 'https://example.com/recording',
                )

        self.assertFalse(checkout.exists())
        self.assertEqual(git(self.local, 'rev-parse', 'HEAD'), head)
        self.assertEqual(git(self.local, 'diff', '--cached'), staged)
        self.assertEqual(git(self.local, 'diff'), unstaged)
        self.assertEqual((self.local / 'released').read_text(), 'untracked draft\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:unrelated'), 'overlapping release\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:released'), 'published version\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:another-release'), 'newer release\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'lecture\nrecording\n')

        published = git(self.remote, 'rev-parse', 'HEAD')
        with recording.publication_checkout(self.local) as checkout:
            with contextlib.redirect_stdout(io.StringIO()):
                recording.run_git_commands(
                    checkout, checkout / 'schedule', 'LEC 12', 'https://example.com/recording',
                )
        self.assertEqual(git(self.remote, 'rev-parse', 'HEAD'), published)

    def test_conflict_keeps_remote_release_and_desktop_checkout(self):
        with recording.publication_checkout(self.local) as checkout:
            (checkout / 'schedule').write_text('recording update\n')
            self.remote_change('schedule', 'concurrent schedule update\n')
            with self.assertRaises(subprocess.CalledProcessError):
                recording.run_git_commands(
                    checkout, checkout / 'schedule', 'LEC 12', 'https://example.com/recording',
                )

        self.assertFalse(checkout.exists())
        self.assertEqual((self.local / 'schedule').read_text(), 'lecture\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'concurrent schedule update\n')

    def test_caption_refresh_publishes_only_caches_and_rebuilds_when_unchanged(self):
        (self.local / 'unrelated').write_text('staged\n')
        git(self.local, 'add', 'unrelated')
        before = git(self.local, 'diff', '--cached')
        with recording.publication_checkout(self.local) as checkout:
            cache = checkout / '_data/lecture-transcripts/lec01.json'
            cache.parent.mkdir(parents=True)
            cache.write_text('{"segments": []}\n')
            recording.run_caption_git_commands(checkout, [str(cache)])
            self.assertEqual(git(self.remote, 'show', 'HEAD:_data/lecture-transcripts/lec01.json'), cache.read_text())
            self.assertEqual(git(self.remote, 'show', 'HEAD:unrelated'), 'original\n')
            self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'lecture\n')
            prior = git(self.remote, 'rev-parse', 'HEAD')
            recording.run_caption_git_commands(checkout, [str(cache)])
            self.assertNotEqual(git(self.remote, 'rev-parse', 'HEAD'), prior)
        self.assertEqual(git(self.local, 'diff', '--cached'), before)

    def test_empty_caption_refresh_still_pushes_a_rebuild_commit(self):
        prior = git(self.remote, 'rev-parse', 'HEAD')
        with recording.publication_checkout(self.local) as checkout:
            recording.run_caption_git_commands(checkout, [])
        self.assertNotEqual(git(self.remote, 'rev-parse', 'HEAD'), prior)
        self.assertEqual(git(self.remote, 'show', 'HEAD:unrelated'), 'original\n')

    def test_caption_publication_rejects_unrelated_paths(self):
        with self.assertRaisesRegex(ValueError, 'only lecture caption caches'):
            recording.run_caption_git_commands(self.local, [str(self.local / 'schedule')])


if __name__ == '__main__':
    unittest.main()
