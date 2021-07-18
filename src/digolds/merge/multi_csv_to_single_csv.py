import os, glob
import pandas as pd

def _parse(args):
    src_path = args.get('--src-path', '.')
    dest_path = args.get('--dest-path', '.')
    output_name = args.get('--output-name', 'your-csv-file-name.csv')
    return [src_path, dest_path, output_name]

def multiple_csv_to_single_csv_df(src_path):
    all_files = glob.glob(os.path.join(src_path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged   = pd.concat(df_from_each_file, ignore_index=True)
    return df_merged

def _multiple_csv_to_single_csv(src_path, dest_path, output_name):
    df_merged = multiple_csv_to_single_csv_df(src_path)
    df_merged.to_csv(os.path.join(dest_path,output_name), index=False)
    return df_merged

name = 'csv-to-csv'

def handler(args):
    _multiple_csv_to_single_csv(*_parse(args))

def operator(df, args):
    return _multiple_csv_to_single_csv(*_parse(args))

if __name__ == "__main__":
    src_path = 'merge/tests'
    dest_path = 'merge/tests'
    output_name = 'final_result.csv'
    operator(None, {
        '--src-path' : src_path,
        '--dest-path' : dest_path,
        '--output-name' : output_name
    })

# https://blog.softhints.com/how-to-merge-multiple-csv-files-with-python/
# https://stackoverflow.com/questions/20845213/how-to-avoid-python-pandas-creating-an-index-in-a-saved-csv