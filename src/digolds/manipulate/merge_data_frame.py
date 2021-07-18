import pandas as pd

def _parse(args):
    dfs = args.get('--dfs')
    on = args.get('--on')
    return [dfs, on]

def _merge_data_frame(df, dfs, on):
    merged_df = df
    for d in dfs:
        merged_df = pd.merge(merged_df, d, how='left', on=on)
    return merged_df

name = 'merge-data-frame'

def operator(df, args):
    return _merge_data_frame(df, *_parse(args))

if __name__ == "__main__": 
    data = [['tom', 10], ['nick', 15], ['juli', 15]] 
    df = pd.DataFrame(data, columns = ['Name', 'Age'])

    data = [['tom', 10, 'M']] 
    df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Gender'])

    data = [['juli', 15, 99]] 
    df2 = pd.DataFrame(data, columns = ['Name', 'Age', 'Grade'])
    args = {
        '--dfs':[df1, df2],
        '--on':['Name','Age']
    }

    operator(df, args)