import unittest
import pandas as pd
from manipulate import filter
from manipulate import rename

class TestManipulation(unittest.TestCase):
    # run before each test
    def setUp(self):
        print('setUp')
        data = [['tom', 10], ['nick', 15], ['juli', 15]] 
        df = pd.DataFrame(data, columns = ['Name', 'Age'])
        self.df = df
    
    # run after each test
    def tearDown(self):
        print('tearDown')

    def test_filter(self):
        print('filter')
        args = {
            '--condition':lambda: self.df['Age'] == 15
        }
        
        df_result = filter.operator(self.df, args)
        self.assertEqual(len(df_result.index), 2, 'The number of Records should be 2')
        self.assertEqual(df_result['Age'].values[0], 15, 'The first record\'s age should be 15')
    
    def test_rename(self):
        print('rename')
        args = {
            '--columns':{
                'Age' : 'age',
                'Name' : 'name'
                }
        }

        df_result = rename.operator(self.df, args)
        self.assertEqual(df_result.columns[0], 'name', 'Name should be name')
        self.assertEqual(df_result.columns[1], 'age', 'Age should be age')

if __name__ == '__main__':
    unittest.main()