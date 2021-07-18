import pandas as pd

def _parse(args):
    condition = args.get('--condition')
    return [condition]

def _filter_out(df, condition):
    return df[condition()].reset_index(drop=True)

name = 'filter'

def operator(df, args):
    return _filter_out(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['juli', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 

    args = {
        '--condition':lambda: df['Age'] == 15
    }

    operator(df, args)