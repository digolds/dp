import pandas as pd

def _parse(args):
    return []

def _drop_empty_row(df):
    return df.dropna(how='all')

name = 'drop-empty-row'

def operator(df, args):
    return _drop_empty_row(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], [None, None]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 
    args = {}
    operator(df, args)