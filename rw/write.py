from pandas.io.excel import ExcelWriter

def dataframe_to_file(df, args):
    file_name = args.get('file_name', '')
    if file_name.endswith('.xlsx'):
        with ExcelWriter(file_name) as ew:
            df.to_excel(ew, sheet_name=args.get('sheet_name'), index=False)
            return df
    else:
        print(f'invalid file: {file_name}')

operator_name = 'write_file'

def operator(df, args):
    return dataframe_to_file(df, args)