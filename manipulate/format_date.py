import pandas as pd

def _parse(args):
    columns = args.get('--columns')
    return [columns]

def _format_date(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], format='%Y%m%d')
    return df

name = 'format-date'

def operator(df, args):
    return _format_date(df, *_parse(args))

if __name__ == "__main__": 
    data = [['20170212', 10], ['20180712', 15], ['20170509', 15]] 
    df = pd.DataFrame(data, columns = ['Date', 'Age']) 

    args = {
        '--columns':['Date']
    }

    operator(df, args)