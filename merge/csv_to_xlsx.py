from rw.read_write import create_data_frame, dataframe_to_file

def parse(args):
    csv_file = args.get('--csv-file', 'data.csv')
    xlsx_file = args.get('--xlsx-file', 'data.xlsx')
    sheet_name = args.get('--sheet-name', 'daily')
    return (csv_file, xlsx_file, sheet_name)

def df_to_xlsx(df, xlsx_file, sheet_name):
    return dataframe_to_file(df, {
        'file_name' : xlsx_file,
        'sheet_name' : sheet_name
    })

def csv_to_xlsx(csv_file, xlsx_file, sheet_name):
    df = create_data_frame(csv_file)
    return df_to_xlsx(df, xlsx_file, sheet_name)

name = 'csv2xlsx'

def handler(args):
    csv_to_xlsx(*parse(args))

if __name__ == "__main__":
    csv_file = 'merge/tests/01.csv'
    xlsx_file = 'merge/tests/final_result.xlsx'
    sheet_name = 'daily'
    csv_to_xlsx(csv_file, xlsx_file, sheet_name)

# https://stackoverflow.com/questions/39099008/how-to-write-csv-files-into-xlsx-using-python-pandas
# https://www.codegrepper.com/code-examples/r/pandas+to+excel+no+index