import pandas as pd

def _parse(args):
    file_name = args.get('--file-name', '')
    return [file_name]

def _dataframe_to_file(df, file_name):
    df.to_csv(file_name, index=False)
    return df

name = 'write-to-csv'

def operator(df, args):
    return _dataframe_to_file(df, *_parse(args))