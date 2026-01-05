import pandas as pd

def clean_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    df["Price"] = df["Price"].fillna(df["Price"].median())
    df["Region"] = df["Region"].fillna("Unknown")

    return df
