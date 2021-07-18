from digolds.rw import write_xlsx
from digolds.merge import multi_csv_to_single_csv
import os

def _parse(args):
    src_path = args.get('--src-path', '.')
    xlsx_file = args.get('--xlsx-file', '')
    sheet_name = args.get('--sheet-name', '')
    return [src_path, xlsx_file, sheet_name]

def _multiple_csv_to_single_xlsx(src_path, xlsx_file, sheet_name):
    csv_df = multi_csv_to_single_csv.multiple_csv_to_single_csv_df(src_path)

    return write_xlsx.operator(csv_df, {
        '--file-name' : xlsx_file,
        '--sheet-name' : sheet_name
    })

name = 'multi-csv-to-xlsx'

def handler(args):
    _multiple_csv_to_single_xlsx(*_parse(args))

def operator(df, args):
    return _multiple_csv_to_single_xlsx(*_parse(args))

if __name__ == "__main__":
    operator(None, {
        '--src-path' : 'merge/tests',
        '--xlsx-file' : 'test.xlsx',
        '--sheet-name' : 'abc'
    })