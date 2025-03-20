import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("res_dpre.csv")

plt.figure(figsize=(8, 5))
plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Distribution of House Prices")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("vis.png")

exec(open("model.py").read())