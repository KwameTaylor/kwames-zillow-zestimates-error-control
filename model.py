import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def create_cluster_area(train, train_scaled, validate, validate_scaled, test, test_scaled, X, Xv, Xt, n_clusters):
    '''
    I'll make this function more generic for more useability on the next pipeline iteration.
    '''
    kmeans = KMeans(n_clusters).fit(X)

    train_scaled['cluster_area'] = kmeans.predict(X)
    train['cluster_area'] = kmeans.predict(X)

    validate_scaled['cluster_area'] = kmeans.predict(Xv)
    validate['cluster_area'] = kmeans.predict(Xv)

    test_scaled['cluster_area'] = kmeans.predict(Xt)
    test['cluster_area'] = kmeans.predict(Xt)

    centroids = pd.DataFrame(kmeans.cluster_centers_, columns=X.columns)

    return kmeans, centroids

def cluster_area_viz(train):
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

def cluster_area_dummies(train):
    area_dummies = pd.get_dummies(train.cluster_area, drop_first=True)
    train = pd.concat([train, area_dummies], axis=1)
    train = train.rename(columns={1: "cluster_area_1", 2: "cluster_area_2", 3: "cluster_area_3", 4: "cluster_area_4", 5: "cluster_area_5"})
    train = train.drop(columns=['cluster_area'])
    return train