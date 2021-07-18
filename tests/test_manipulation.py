import unittest
import pandas as pd
from digolds.manipulate import filter
from digolds.manipulate import rename
from digolds.manipulate import drive_new_column
from digolds.manipulate import drop_empty_row
from digolds.manipulate import drop_duplicate_row
from digolds.manipulate import merge_data_frame
from digolds.manipulate import format_date
from digolds.manipulate import drop_column

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
        self.assertFalse(df_result.equals(self.df), 'filter should do nothing on input data frame')
    
    def test_drop_column(self):
        args = {
            '--columns':['Age'],
            '--remain' : True
        }
        df_result = drop_column.operator(self.df, args)
        self.assertTrue(df_result.columns[0] == self.df.columns[1], 'Column name should be Age')

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
    
    def test_drive_new_column(self):
        args = {
            '--new-column-name' : 'name-age',
            '--shape-func' : lambda row: row['Name'] + '-' + str(row['Age'])
        }
        df_result = drive_new_column.operator(self.df, args)
        self.assertEqual(df_result.columns[2], 'name-age', 'New column name should be name-age')
    
    def test_drop_empty_row(self):
        data = [['tom', 10], ['nick', 15], [None, None]] 
        df = pd.DataFrame(data, columns = ['Name', 'Age']) 
        args = {}
        df_result = drop_empty_row.operator(df, args)
        self.assertEqual(len(df_result.index), 2, 'The number of records should be 2')
    
    def test_drop_duplicate_row(self):
        data = [['tom', 10], ['nick', 15], ['nick', 15]] 
        df = pd.DataFrame(data, columns = ['Name', 'Age']) 
        args = {
            '--subset':['Name', 'Age']
        }
        df_result = drop_duplicate_row.operator(df, args)
        self.assertEqual(len(df_result.index), 2, 'The number of records should be 2')
    
    def test_merge_data_frame(self):
        data = [['tom', 10], ['nick', 15], ['juli', 15]] 
        df = pd.DataFrame(data, columns = ['Name', 'Age'])
        data = [['tom', 10, 'M']] 
        df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Gender'])
        data = [['juli', 15, 99]] 
        df2 = pd.DataFrame(data, columns = ['Name', 'Age', 'Grade'])
        args = {
            '--dfs':[df1, df2],
            '--on':['Name','Age']
        }
        df_result = merge_data_frame.operator(df, args)
        self.assertTrue(df_result['Gender'].isnull().values[1])
        self.assertTrue(df_result['Grade'].isnull().values[1])
    
    def test_format_date(self):
        data = [['20170212', 10], ['20180712', 15], ['20170509', 15]] 
        df = pd.DataFrame(data, columns = ['Date', 'Age']) 
        args = {
            '--columns':['Date']
        }
        df_result = format_date.operator(df, args)
        import numpy as np
        self.assertTrue(type(df_result['Date'].values[0]) == np.datetime64)

if __name__ == '__main__':
    unittest.main()