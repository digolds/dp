import os, glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name = 'bar'

def handler(args):
    file_name = args.get('--file-name', '')
    image_name = args.get('--image-name', 'tmp.png')
    df = pd.read_excel(file_name)
    pivot = pd.pivot_table(df, 
                       index=['Type'], 
                       columns='Region', 
                       values='Amount', 
                       aggfunc='sum',
                       fill_value=0)

    pivot.plot.bar(stacked=True)
    plt.savefig(image_name, dpi=300, bbox_inches='tight')
    plt.show()
    ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()


if __name__ == "__main__":
    args = {
        '--file-name':'./tests/bar-data.xlsx',
        '--image-name': 'plot.png'
    }
    handler(args)

# https://towardsdatascience.com/use-python-to-automate-your-excel-work-c16b6e5ab58e?gi=3f52a4063703