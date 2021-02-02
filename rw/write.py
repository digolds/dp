from pandas.io.excel import ExcelWriter

def _parse(args):
    file_name = args.get('--file-name', '')
    sheet_name = args.get('--sheet-name', '')
    return (file_name, sheet_name)

def _dataframe_to_file(df, file_name, sheet_name):
    with ExcelWriter(file_name) as ew:
        df.to_excel(ew, sheet_name=sheet_name, index=False)
        return df

name = 'write2xlsx'

def operator(df, args):
    return _dataframe_to_file(df, *_parse(args))