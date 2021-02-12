import unittest
from convert.ppt_to_pdf import operator

class TestPPTToPDF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pathlib
        cls.test_root = pathlib.Path.cwd()

    def test_ppt_to_pdf(self):
        output = self.test_root / 'convert/tests/result.pdf'
        args = {
        '--input-file-name': str(self.test_root / 'convert/tests/result.pptx'),
        '--output-file-name': str(output),
        }
        operator(None, args)
        self.assertTrue(output.exists(), 'Successfully convert pptx to pdf')
        output.unlink() #remove pdf file

if __name__ == '__main__':
    unittest.main()