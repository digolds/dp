import pandas as pd

def _parse(args):
    subset = args.get('--subset')
    return [subset]

def _drop_duplicate_row(df, subset):
    df.drop_duplicates(subset, keep='first', inplace= True)
    return df

name = 'drop-duplicate-row'

def operator(df, args):
    return _drop_duplicate_row(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['nick', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 
    args = {
        '--subset' : ['Name']
    }
    operator(df, args)