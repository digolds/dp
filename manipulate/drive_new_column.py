import pandas as pd

def _parse(args):
    new_column_name = args.get('--new-column-name')
    shape_func = args.get('--shape-func')
    return [new_column_name, shape_func]

def _drive_new_column(df, new_column_name, shape_func):
    df[new_column_name] = df.apply(shape_func, axis=1)
    return df

name = 'drive-new-column'

def operator(df, args):
    return _drive_new_column(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['juli', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 

    args = {
        '--new-column-name' : 'name-age',
        '--shape-func' : lambda row: row['Name'] + '-' + str(row['Age'])
    }

    operator(df, args)