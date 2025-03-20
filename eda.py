import pandas as pd

df = pd.read_csv("res_dpre.csv")

avg_price = df['price'].mean()# Insight 1
avg_bedrooms = df['bedrooms'].mean()# Insight 2
avg_bathrooms = df['bathrooms'].mean()# Insight 3

with open("eda-in-1.txt", "w") as f:
    f.write(f"Average Price: {avg_price}\n")

with open("eda-in-2.txt", "w") as f:
    f.write(f"Average Bedrooms: {avg_bedrooms}\n")

with open("eda-in-3.txt", "w") as f:
    f.write(f"Average Bathrooms: {avg_bathrooms}\n")

exec(open("vis.py").read())