import unittest
from ppt.sync_image import operator

class TestSyncImageToPPT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pathlib
        cls.test_root = pathlib.Path.cwd()

    def test_ppt_to_pdf(self):
        pptfile = self.test_root / 'ppt/tests/sample.pptx'
        new_image_file = self.test_root / 'ppt/tests/index.jpg'
        args = {
            '--ppt-file' : str(pptfile),
            '--slide-no': 0,
            '--image-name' : 'Icon_Bird_512x512.png',
            '--new-image-file' : str(new_image_file)
        }
        operator(None, args)

if __name__ == '__main__':
    unittest.main()