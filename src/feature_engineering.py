import pandas as pd

def add_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalSales"] = df["Quantity"] * df["Price"]
    return df
