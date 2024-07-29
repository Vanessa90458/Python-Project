import pandas as pd

def clean_transform_data(data):
    df = pd.DataFrame(data)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['availability'] = df['availability'].str.lower()
    return df
