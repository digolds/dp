import pandas as pd

def _parse(args):
    file_name = args.get('--file-name', '')
    return (file_name,)

def _create_data_frame(file_name):
    return pd.read_csv(file_name)

name = 'read-from-csv'

def operator(df, args):
    return _create_data_frame(*_parse(args))