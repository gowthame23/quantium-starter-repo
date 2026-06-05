import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    df = df[df["product"] == "pink morsel"]

    df["sales"] = df["quantity"] * df["price"]

    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs)

final_df.to_csv("formatted_sales_data.csv", index=False)

print("Output file created successfully!")