import pandas as pd
from pandas.io.excel import ExcelWriter

def create_data_frame(file_name):
    if file_name.endswith('.xlsx'):
        return pd.read_excel(file_name)
    elif file_name.endswith('.csv'):
        return pd.read_csv(file_name)

def dataframe_to_file(df, args):
    if args.get('file_name').endswith('.xlsx'):
        with ExcelWriter(args.get('file_name')) as ew:
            df.to_excel(ew, sheet_name=args.get('sheet_name'), index=False)
            return df