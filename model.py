import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def create_cluster1(X_train_scaled, X, n_clusters):
    kmeans = KMeans(n_clusters).fit(X)
    X_train_scaled['cluster'] = kmeans.predict(X)
    centroids = pd.DataFrame(kmeans.cluster_centers_, columns=X.columns)
    return kmeans, centroids

def cluster1_viz(train):
    fig, ax = plt.subplots(figsize=(13, 7))

    for cluster, subset in train.groupby('cluster'):
        ax.scatter(subset.sepal_width, subset.sepal_length, label=cluster)
    ax.legend(title='cluster')
    ax.set(ylabel='sepal length', xlabel='sepal width')

    train.groupby('cluster').mean().plot.scatter(y='sepal_length', x='sepal_width', marker='x', s=5000, ax=ax, c='black')
    plt.show()

def choose_k(kmeans, X):
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

def intertia_k(X):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(9, 6))
        pd.Series({k: KMeans(k).fit(X).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('The elbow method -\nChange in inertia as k increases')