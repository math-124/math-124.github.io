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
        subprocess.check_call(['git', 'init', '--bare', '-q', str(self.remote)])
        self.local = root / 'local'
        self.other = root / 'other'
        git(root, 'clone', str(self.remote), str(self.local))
        for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
            git(self.local, 'config', key, value)
        (self.local / 'schedule').write_text('lecture\n')
        (self.local / 'unrelated').write_text('original\n')
        git(self.local, 'add', '.')
        git(self.local, 'commit', '-m', 'Initial')
        git(self.local, 'push', '-u', 'origin', 'HEAD')
        git(root, 'clone', str(self.remote), str(self.other))
        for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
            git(self.other, 'config', key, value)
        original = recording.REPO_ROOT
        recording.REPO_ROOT = str(self.local)
        self.addCleanup(setattr, recording, 'REPO_ROOT', original)

    def publish(self):
        with contextlib.redirect_stdout(io.StringIO()):
            recording.run_git_commands(str(self.local / 'schedule'), 'LEC 12', 'https://example.com/recording')

    def remote_change(self, filename, text):
        (self.other / filename).write_text(text)
        git(self.other, 'add', filename)
        git(self.other, 'commit', '-m', 'Remote update')
        git(self.other, 'push')

    def test_sync_publish_and_unchanged_retry_preserve_staged_edits(self):
        (self.local / 'unrelated').write_text('staged\n')
        git(self.local, 'add', 'unrelated')
        (self.local / 'unrelated').write_text('staged plus unstaged\n')
        before = git(self.local, 'diff', '--cached')
        self.remote_change('released', 'Lab 6\n')
        (self.local / 'schedule').write_text('lecture\nrecording\n')
        self.publish()
        self.assertEqual(git(self.local, 'diff', '--cached'), before)
        self.assertEqual((self.local / 'unrelated').read_text(), 'staged plus unstaged\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:unrelated'), 'original\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'lecture\nrecording\n')
        self.assertTrue((self.local / 'released').exists())
        # Simulate a successful local commit whose push never happened.
        (self.local / 'schedule').write_text('lecture\nrecording retry\n')
        git(self.local, 'commit', '--only', '-m', 'Pending recording', '--', 'schedule')
        self.publish()
        self.publish()
        self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'lecture\nrecording retry\n')
        self.assertEqual(git(self.local, 'diff', '--cached'), before)

    def test_conflict_aborts_and_restores_staging(self):
        self.remote_change('schedule', 'remote lecture\n')
        (self.local / 'schedule').write_text('local lecture\n')
        git(self.local, 'commit', '--only', '-m', 'Local update', '--', 'schedule')
        (self.local / 'unrelated').write_text('staged\n')
        git(self.local, 'add', 'unrelated')
        before = git(self.local, 'diff', '--cached')
        with self.assertRaisesRegex(RuntimeError, 'conflict'):
            recording.synchronize_git()
        self.assertEqual(git(self.local, 'diff', '--cached'), before)
        self.assertEqual((self.local / 'schedule').read_text(), 'local lecture\n')
        self.assertEqual(git(self.remote, 'show', 'HEAD:schedule'), 'remote lecture\n')


if __name__ == '__main__':
    unittest.main()
