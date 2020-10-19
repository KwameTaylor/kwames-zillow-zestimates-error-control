import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster1(train, X, n_clusters):
#   X = train_scaled[['sepal_width', 'sepal_length']]
#n_clusters=5
    kmeans = KMeans(n_clusters).fit(X)

    print(pd.DataFrame(kmeans.cluster_centers_, columns=X.columns))

    print(X.shape)

    print(kmeans.labels_.shape)

    train['cluster'] = kmeans.labels_

def cluster1_viz(train):
    fig, ax = plt.subplots(figsize=(13, 7))

    for cluster, subset in train.groupby('cluster'):
        ax.scatter(subset.sepal_width, subset.sepal_length, label=cluster)
    ax.legend(title='cluster')
    ax.set(ylabel='sepal length', xlabel='sepal width')

    train.groupby('cluster').mean().plot.scatter(y='sepal_length', x='sepal_width', marker='x', s=5000, ax=ax, c='black')
    plt.show()

def choose_k(X):
    # sum of squared distances from each point to its cluster center
    kmeans.inertia_

    output = {}

    for k in range(1, 12):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        output[k] = kmeans.inertia_

    ax = pd.Series(output).plot(figsize=(13, 7))
    ax.set(xlabel='k', ylabel='inertia', xticks=range(1, 12), title='The elbow method for determining k')
    ax.grid()