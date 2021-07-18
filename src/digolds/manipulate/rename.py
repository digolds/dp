import pandas as pd

def _parse(args):
    columns = args.get('--columns')
    return [columns]

def _filter_out(df, columns):
    df.rename(columns=columns, inplace=True)
    return df

name = 'rename'

def operator(df, args):
    return _filter_out(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['juli', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 

    args = {
        '--columns':{
            'Age' : 'age',
            'Name' : 'name'
            }
    }

    operator(df, args)