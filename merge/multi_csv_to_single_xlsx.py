from merge import csv_to_xlsx
from merge import multi_csv_to_single_csv
import os

def _parse(args):
    src_path = args.get('--src-path', '.')
    xlsx_file = args.get('--xlsx-file', 'data.xlsx')
    sheet_name = args.get('--sheet-name', 'daily')
    return (src_path, xlsx_file, sheet_name)

def _multiple_csv_to_single_xlsx(src_path, xlsx_file, sheet_name):
    dest_path = '.'
    output_name = 'digolds-dp.csv'
    csv_file = multi_csv_to_single_csv.operator(None, {
        '--src-path' : src_path,
        '--dest-path' : dest_path,
        '--output-name' : output_name
    })
    output = csv_to_xlsx.operator(None, {
        '--csv-file' : csv_file,
        '--xlsx-file' : xlsx_file,
        '--sheet-name' : sheet_name
    })
    file_name = os.path.join(dest_path,output_name)
    if os.path.exists(file_name):
        os.remove(file_name)
    return output

name = 'multi-csv2xlsx'

def handler(args):
    _multiple_csv_to_single_xlsx(*_parse(args))

def operator(df, args):
    return _multiple_csv_to_single_xlsx(*_parse(args))

if __name__ == "__main__":
    pass