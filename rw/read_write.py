import pandas as pd

def create_data_frame(file_name):
    if file_name.endswith('.xlsx'):
        return pd.read_excel(file_name)
    elif file_name.endswith('.csv'):
        return pd.read_csv(file_name)