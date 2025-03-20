import pandas as pd
import sys

file_path = sys.argv[1]
df = pd.read_csv(file_path)
df.to_csv("loaded_data.csv", index=False)
print("Data loaded successfully.")

exec(open("dpre.py").read())
