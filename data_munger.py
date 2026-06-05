import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Convert price from "$3.00" to 3.00
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs)

final_df.to_csv("formatted_data.csv", index=False)

print("Output file created successfully!")