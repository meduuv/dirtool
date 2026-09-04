import tempfile,unittest
from pathlib import Path
from dirtool import entries,files,dirs
class Tests(unittest.TestCase):
 def test_scan(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/"a").write_text("x");(p/"sub").mkdir()
   self.assertEqual(entries(p),["a","sub"]);self.assertEqual(files(p),["a"]);self.assertEqual(dirs(p),["sub"])
if __name__=="__main__":unittest.main()
