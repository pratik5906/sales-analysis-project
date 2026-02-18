import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = {
    "Order_ID": np.arange(1, rows+1),
    "Date": pd.date_range(start="2024-01-01", periods=rows, freq="D"),
    "Category": np.random.choice(["Electronics", "Fashion", "Home Decor", "Grocery"], rows),
    "Sub_Category": np.random.choice(["A", "B", "C", "D"], rows),
    "Region": np.random.choice(["North", "South", "East", "West"], rows),
    "Sales": np.random.randint(500, 5000, rows),
    "Profit": np.random.randint(50, 1000, rows),
    "Quantity": np.random.randint(1, 10, rows),
    "Discount": np.random.uniform(0, 0.3, rows)
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

print("Dataset Generated Successfully!")