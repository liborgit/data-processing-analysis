import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

sales_over_time = df.groupby("Date")["Sales"].sum()

sales_over_time.plot(kind="line")
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()