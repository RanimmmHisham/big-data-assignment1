import pandas as pd

df = pd.read_csv("loaded_data.csv")

# Data Cleaning
df = df.dropna()

# Data Transformation
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
if categorical_cols:
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Data Reduction
df = df.drop_duplicates()

# Data Discretization: Bin 'price' column into 4 quantiles
if 'price' in df.columns:
    df['price_bin'] = pd.qcut(df['price'], q=4, labels=False)

df.to_csv("res_dpre.csv", index=False)

exec(open("eda.py").read())