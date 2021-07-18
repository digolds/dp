import unittest
from digolds.common import create_operator

class TestCommon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pathlib
        cls.test_root = pathlib.Path.cwd() / 'data'

    def test_common(self):
        csv_file = self.test_root / 'common/01.csv'
        read_operator = create_operator(
            {
                '--file-name' : csv_file
            },
            'read-from-csv')
        df = read_operator()

if __name__ == '__main__':
    unittest.main()