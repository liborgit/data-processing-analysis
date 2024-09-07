import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sales_by_category = df.groupby("Category")["Sales"].sum()

print(sales_by_category)

sales_by_category.plot(kind="bar")
plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()