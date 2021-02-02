import os
import importlib
import glob

class Operator:
    def __init__(self, in_df, in_args, callable_core):
        self.in_df = in_df
        self.in_args = in_args
        self.callable_core = callable_core
        self.out_df = None

    def __call__(self):
        self.out_df = self.callable_core(self.in_df, self.in_args)
        return self.out_df

def get_operators(sub_folder):
    dirpath = os.path.join(os.path.dirname(__file__), sub_folder)
    foldername = os.path.basename(dirpath)
    files = [f for f in glob.glob(os.path.join(dirpath, '*.py'))]
    operator_map = {}
    for f in files:
        f = os.path.basename(f)
        if f == '__init__.py':
            continue
        f_without_extension = os.path.splitext(f)[0]
        m = importlib.import_module(f'{foldername}.{f_without_extension}')
        operator_map[getattr(m, 'operator_name')] = getattr(m, 'operator')
    return operator_map

def get_all_operators():
    return get_operators('rw')

def create_operator(name, df, args):
    ops = get_all_operators()
    return Operator(df, args, ops[name])

if __name__ == '__main__':
    read_operator = create_operator('read_file', None, {
        'file_name' : r'D:\dr\dp\merge\tests\01.csv'
    })
    df = read_operator()

    write_operator = create_operator('write_file', df, {
        'file_name' : 'abc.xlsx',
        'sheet_name' : 'abc'
    })
    df = write_operator()