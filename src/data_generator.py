import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_retail_data(num_rows: int = 80) -> pd.DataFrame:
    np.random.seed(42)

    products = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"]
    categories = {
        "Laptop": "Electronics",
        "Phone": "Electronics",
        "Tablet": "Electronics",
        "Headphones": "Accessories",
        "Smartwatch": "Accessories"
    }
    regions = ["North", "South", "East", "West"]

    start_date = datetime(2024, 1, 1)

    data = {
        "TransactionID": np.arange(1, num_rows + 1),
        "Date": [start_date + timedelta(days=np.random.randint(0, 90)) for _ in range(num_rows)],
        "Product": np.random.choice(products, num_rows),
        "Region": np.random.choice(regions, num_rows),
        "Quantity": np.random.randint(1, 6, num_rows),
        "Price": np.random.randint(100, 1500, num_rows),
        "CustomerID": np.random.randint(1000, 1100, num_rows)
    }

    df = pd.DataFrame(data)
    df["Category"] = df["Product"].map(categories)

    # Introduce dirty data
    df.loc[5, "Price"] = None
    df.loc[12, "Region"] = None
    df = pd.concat([df, df.iloc[[10]]], ignore_index=True)

    return df