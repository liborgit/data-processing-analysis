import pandas as pd

df = pd.read_csv("sales.csv")

max_sales_product = df.loc[df["Sales"].idxmax()]
min_sales_product = df.loc[df["Sales"].idxmin()]

print(f"Product with highest sales:\n{max_sales_product}")
print(f"Product with lowest sales:\n{min_sales_product}")