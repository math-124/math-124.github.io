import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from recording_captions import refresh_captions, _captions_are_processing

VTT = b'WEBVTT\n\n00:00:01.000 --> 00:00:04.000\nMatrix columns.\n\n00:00:40.000 --> 00:00:43.000\nLinear maps.\n'
TARGET = dict(recording_url='https://leccap.engin.umich.edu/leccap/player/r/Example',lecture_number='11')

class Captions(unittest.TestCase):
 def test_processing_notice_requires_the_target_player_not_a_login_page(self):
  ctx=Mock(); page=ctx.new_page.return_value; page.url=TARGET['recording_url']
  notice=page.get_by_text.return_value;notice.count.return_value=1
  self.assertTrue(_captions_are_processing(ctx,TARGET['recording_url']))
  notice.wait_for.assert_called_with(state='attached',timeout=5000)
  page.url='https://okta.umich.edu/signin'
  self.assertFalse(_captions_are_processing(ctx,TARGET['recording_url']))
 def test_confirmed_processing_preserves_cache_and_can_be_retried(self):
  with tempfile.TemporaryDirectory() as tmp:
   ctx=Mock(); ctx.request.get.return_value.ok=True; ctx.request.get.return_value.body.return_value=VTT
   paths=refresh_captions(ctx,TARGET,tmp,'124')
   saved=[Path(p).read_bytes() for p in paths]
   ctx.request.get.return_value.body.return_value=b''
   with patch('recording_captions._captions_are_processing', return_value=True):
    self.assertEqual(refresh_captions(ctx,TARGET,tmp,'124'), [])
   self.assertEqual([Path(p).read_bytes() for p in paths],saved)
   ctx.request.get.return_value.body.return_value=VTT.replace(b'Matrix columns.',b'Ready captions.')
   self.assertEqual(refresh_captions(ctx,TARGET,tmp,'124'),paths)
   self.assertNotEqual([Path(p).read_bytes() for p in paths],saved)
 def test_unconfirmed_http_failure_still_blocks_publication(self):
  with tempfile.TemporaryDirectory() as tmp:
   ctx=Mock();ctx.request.get.return_value.ok=False;ctx.request.get.return_value.status=500
   with patch('recording_captions._captions_are_processing', return_value=False):
    with self.assertRaisesRegex(RuntimeError,'HTTP 500'):
     refresh_captions(ctx,TARGET,tmp,'124')
   self.assertEqual(list(Path(tmp).rglob('*.json')),[])
 def test_download_retry_revision_and_invalid_response(self):
  for course in ('124','245'):
   with self.subTest(course=course), tempfile.TemporaryDirectory() as tmp:
    ctx=Mock(); ctx.request.get.return_value.ok=True; ctx.request.get.return_value.body.return_value=VTT
    paths=refresh_captions(ctx,TARGET,tmp,course)
    saved=[Path(p).read_bytes() for p in paths]
    self.assertEqual(refresh_captions(ctx,TARGET,tmp,course), paths)
    self.assertEqual([Path(p).read_bytes() for p in paths],saved)
    self.assertEqual(ctx.request.get.call_count,2)
    ctx.request.get.return_value.body.return_value=b'<html>Sign in</html>'
    with self.assertRaises(ValueError): refresh_captions(ctx,TARGET,tmp,course)
    self.assertEqual([Path(p).read_bytes() for p in paths],saved)
    ctx.request.get.return_value.body.return_value=VTT.replace(b'Matrix columns.',b'Updated captions.')
    refresh_captions(ctx,TARGET,tmp,course)
    self.assertNotEqual([Path(p).read_bytes() for p in paths],saved)
 def test_preserve_reviewed_bounds(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'_data/lecture-transcripts/lec11.json'; p.parent.mkdir(parents=True)
   p.write_text(json.dumps(dict(recording=TARGET['recording_url'],lectureRange=dict(start=30,end=60))))
   ctx=Mock();ctx.request.get.return_value.ok=True;ctx.request.get.return_value.body.return_value=VTT
   refresh_captions(ctx,TARGET,tmp,'124')
   result=json.loads(p.read_text()); self.assertEqual(result['lectureRange'],dict(start=30,end=60))
   self.assertEqual(result['segments'][0]['text'],'Linear maps.')

if __name__ == '__main__':
 unittest.main()
