import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def parse(args):
    file_name = args.get('--file-name', '')
    image_name = args.get('--image-name', 'tmp.png')
    index = map(str.strip, args.get('--index', '').split(','))
    columns = args.get('--columns', '')
    values = args.get('--values', '')
    show = args.get('--show', '')
    return (file_name, image_name, index, columns, values, show)

def draw_bar(file_name, image_name, index, columns, values, show):
    df = pd.read_excel(file_name)
    pivot = pd.pivot_table(df,
                       index=index, 
                       columns=columns, 
                       values=values, 
                       aggfunc='sum',
                       fill_value=0)

    pivot.plot.bar(stacked=True)
    if show == 'yes':
        plt.show()
    else:
        plt.savefig(image_name, dpi=300, bbox_inches='tight')

name = 'bar'

def handler(args):
    draw_bar(*parse(args))
    # ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
    # ts = ts.cumsum()
    # ts.plot()
    # plt.show()


if __name__ == "__main__":
    args = {
        '--file-name':'./tests/bar-data.xlsx',
        '--image-name': 'plot.png',
        '--index': 'Date,Type',
        '--columns' : 'Region',
        '--values' : 'Amount',
        '--show' : 'yes'
    }
    handler(args)

# https://towardsdatascience.com/use-python-to-automate-your-excel-work-c16b6e5ab58e?gi=3f52a4063703