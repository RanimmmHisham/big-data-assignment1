Housing Data Processing Pipeline

Project Overview

This project builds a Dockerized pipeline for processing housing data. The pipeline includes data loading, preprocessing, exploratory data analysis (EDA), visualization, and clustering using K-Means.

Setup and Execution

1. Create the Project Directory

mkdir bd-a1
cd bd-a1

2. Download and Place the Dataset

Download a dataset and place it inside the bd-a1/ directory.

3. Create the Dockerfile

Create a Dockerfile in bd-a1/ with the following content:

FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --break-system-packages pandas numpy seaborn matplotlib scikit-learn scipy
RUN mkdir -p /home/doc-bd-a1/
WORKDIR /home/doc-bd-a1/
COPY Housing.csv /home/doc-bd-a1/
CMD ["/bin/bash"]

4. Build the Docker Image

docker build -t bd-a1-image .

5. Run the Container

docker run -it --name bd-a1-container bd-a1-image

6. Create Python Scripts Inside the Container

Inside the container, create the following scripts:

load.py

nano load.py

import pandas as pd
import sys

file_path = sys.argv[1]
df = pd.read_csv(file_path)
df.to_csv("loaded_data.csv", index=False)
print("Data loaded successfully.")

exec(open("dpre.py").read())
dpre.py

nano dpre.py

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
eda.py

nano eda.py

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
vis.py

nano vis.py

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
model.py

nano model.py

import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("res_dpre.csv")

features = df[['price', 'bedrooms', 'bathrooms']]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(features)
df['cluster'] = kmeans.labels_

cluster_counts = df['cluster'].value_counts()
with open("k.txt", "w") as f:
    for cluster, count in cluster_counts.items():
        f.write(f"Cluster {cluster}: {count} records\n")

final.sh

mkdir -p service-result/

CONTAINER_NAME=bd-a1-container

docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_dpre.csv service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt service-result/

docker stop $CONTAINER_NAME
7. Execute the Pipeline

Run the following command inside the container:

python3 load.py /home/doc-bd-a1/Housing.csv

8. Copy Output Files and Stop Container

Run the final script from outside the container:

bash final.sh

Output Files

res_dpre.csv - Processed dataset

eda-in-1.txt - Average Price

eda-in-2.txt - Average Bedrooms

eda-in-3.txt - Average Bathrooms

vis.png - Data visualization

k.txt - K-Means cluster results
