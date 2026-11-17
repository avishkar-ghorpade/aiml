import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
mall_data = pd.read_csv("/home/avcoe/Mall_Customers.csv")
print(mall_data.head())
print(mall_data.info())
corr = mall_data.corr(numeric_only=True)
plt.figure(figsize=(8, 8))
sns.heatmap(corr, cbar=True, square=True, fmt='.1f',
            annot=True, cmap='Reds')
plt.title("Correlation Heatmap")
plt.show()
plt.figure(figsize=(10, 10))
sns.countplot(x="Gender", data=mall_data)
plt.title("Gender Distribution")
plt.show()
plt.figure(figsize=(16, 10))
sns.countplot(x="Age", data=mall_data)
plt.title("Age Distribution")
plt.show()
plt.figure(figsize=(20, 8))
sns.barplot(x='Annual Income (k$)',
            y='Spending Score (1-100)', data=mall_data)
plt.title("Annual Income vs Spending Score")
plt.show()
X = mall_data.iloc[:, [2, 3, 4]].values
plt.figure(figsize=(12, 7))
linked = linkage(X, method='ward')
dendrogram(linked)
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
hc = AgglomerativeClustering(n_clusters=5, linkage='ward')
y_hc = hc.fit_predict(X)
# 3D Visualization
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1],
           X[y_hc == 0, 2], s=40, color='red',
           label='Cluster 1')
ax.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1],
           X[y_hc == 1, 2], s=40, color='blue',
           label='Cluster 2')
ax.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1],
           X[y_hc == 2, 2], s=40, color='green',
           label='Cluster 3')
ax.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1],
           X[y_hc == 3, 2], s=40, color='yellow',
           label='Cluster 4')
ax.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1],
           X[y_hc == 4, 2], s=40, color='purple',
           label='Cluster 5')
ax.set_xlabel('Age of a Customer')
ax.set_ylabel('Annual Income')
ax.set_zlabel('Spending Score')
ax.set_title('Hierarchical Clustering')
ax.legend()
plt.show()
