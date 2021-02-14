import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from rw import read_csv

def _parse(args):
    image_name = args.get('--image-name', 'tmp.png')
    index = map(str.strip, args.get('--index', '').split(','))
    columns = args.get('--columns', '')
    values = args.get('--values', '')
    show = args.get('--show', '')
    return [image_name, index, columns, values, show]

def draw_bar_df(df, image_name, index, columns, values, show):
    pivot = pd.pivot_table(df,
                       index=index, 
                       columns=columns, 
                       values=values, 
                       aggfunc='sum',
                       fill_value=0)

    pivot.plot.bar(rot=45)
    if show == 'yes':
        plt.show()
    else:
        plt.savefig(image_name, dpi=300, bbox_inches='tight')
    return df

def draw_bar(file_name, image_name, index, columns, values, show):
    df = read_csv.operator(None, {
        '--file-name' : file_name
    })
    return draw_bar_df(df, image_name, index, columns, values, show)

name = 'bar'

def handler(args):
    file_name = args.get('--file-name', '')
    append_args = [file_name] + _parse(args)
    draw_bar(*append_args)
    # ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
    # ts = ts.cumsum()
    # ts.plot()
    # plt.show()

def operator(df, args):
    return draw_bar_df(df, *_parse(args))

if __name__ == "__main__":
    args = {
        '--file-name':'draw/tests/bar-data.xlsx',
        '--image-name': 'plot.png',
        '--index': 'Date,Type',
        '--columns' : 'Region',
        '--values' : 'Amount',
        '--show' : 'yes'
    }
    handler(args)

# https://towardsdatascience.com/use-python-to-automate-your-excel-work-c16b6e5ab58e?gi=3f52a4063703