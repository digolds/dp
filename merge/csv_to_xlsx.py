from rw import read_csv
from rw import write_xlsx

def _parse(args):
    csv_file = args.get('--csv-file', 'data.csv')
    xlsx_file = args.get('--xlsx-file', 'data.xlsx')
    sheet_name = args.get('--sheet-name', 'daily')
    return [csv_file, xlsx_file, sheet_name]

def _csv_to_xlsx(csv_file, xlsx_file, sheet_name):
    df = read_csv.operator(None, {
        '--file-name' : csv_file
    })
    return write_xlsx.operator(df, {
        '--file-name' : xlsx_file,
        '--sheet-name' : sheet_name
    })

name = 'csv-to-xlsx'

def handler(args):
    _csv_to_xlsx(*_parse(args))

def operator(df, args):
    return _csv_to_xlsx(*_parse(args))

if __name__ == "__main__":
    csv_file = 'merge/tests/01.csv'
    xlsx_file = 'merge/tests/final_result.xlsx'
    sheet_name = 'daily'
    operator(None, {
        '--csv-file' : csv_file,
        '--xlsx-file' : xlsx_file,
        '--sheet-name' : sheet_name
    })

# https://stackoverflow.com/questions/39099008/how-to-write-csv-files-into-xlsx-using-python-pandas
# https://www.codegrepper.com/code-examples/r/pandas+to+excel+no+index