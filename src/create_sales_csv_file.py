import pandas as pd
import numpy as np
from random import choice, randint
from datetime import datetime, timedelta

np.random.seed(42)

num_records = 1000

product_names = ["Laptop", "Tablet", "Smartphone", "TV", "Headphones", "Camera", "Smartwatch"]
categories = ["Electronics", "Appliances", "Accessories"]

def generate_sales_data(num_records):
    data = []
    start_date = datetime.now() - timedelta(days=365)
    for i in range(num_records):
        product_name = choice(product_names)
        category = choice(categories)
        sales = randint(1, 100)
        date = start_date + timedelta(days=randint(0, 365))
        data.append([i + 1, product_name, category, sales, date])

    df = pd.DataFrame(data, columns=["Product ID", "Product Name", "Category", "Sales", "Date"])
    return df

df = generate_sales_data(num_records)

df.to_csv("sales.csv", index=False)

print(df.head())