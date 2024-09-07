import pandas as pd

df = pd.read_csv("sales.csv")

average_sales = df["Sales"].mean()
print(f"Average sales: {average_sales}")