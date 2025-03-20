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