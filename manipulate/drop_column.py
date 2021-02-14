import pandas as pd

def _parse(args):
    columns = args.get('--columns')
    remain = args.get('--remain', False)
    return [columns, remain]

def _drop_column(df, columns, remain):
    if remain:
        return df.filter(columns, axis=1).reset_index(drop=True)
    else:
        return df.drop(columns, axis=1).reset_index(drop=True)

name = 'drop-column'

def operator(df, args):
    return _drop_column(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['juli', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 

    args = {
        '--columns':[
            'Age',
            'Name'
        ]
    }

    operator(df, args)