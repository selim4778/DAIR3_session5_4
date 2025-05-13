def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def summarize_data(df):
    return df.describe()
