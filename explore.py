# import necessary packages/modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import sqrt
from sklearn.cluster import KMeans

# default viz size settings
plt.rc('figure', figsize=(10, 8))
plt.rc('font', size=15)

# default pandas decimal number display format
pd.options.display.float_format = '{:20,.2f}'.format

def viz_logerror(train):
    '''
    This functions visualizes log error distribution.
    Takes a dataFrame as an argument.
    '''
    # visualize logerror
    sns.scatterplot(range(train.shape[0]), np.sort(train.logerror.values), color='green', linewidth=0 , s=30)
    plt.xlabel('index')
    plt.ylabel('logerror')
    plt.title('Distribution of Logerror')
    plt.show()

def corr_heatmap(train_scaled):
    '''
    This function creates a heatmap of the correlation of all features scaled, minus longitude and latitude and redundant features.
    Takes a dataFrame as an argument
    '''
    # heatmap time!
    heatmap_data = train_scaled.drop(columns=['latitude', 'longitude', 'decade', 'century'])
    corr = heatmap_data.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    ax = sns.heatmap(corr, mask=mask, center=0, vmin=0, vmax=1, cmap=sns.diverging_palette(95, 220, n=250, s=93, l=35), square=True) 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, horizontalalignment='right')
    plt.title('Which features have significant correlation?')
    ax

def ttest_viz(train):
    '''
    This function creates the visualizations for the T-test and compares the median and means so we can move on to hypothesis testing.
    '''
    prop_1960s = train[train.decade == 196.00]

    sns.distplot(train.logerror)
    plt.title('Overall Log Error')
    #get rid of outliers on a later iteration
    plt.show()

    sns.distplot(prop_1960s.logerror)
    plt.title('Log Error of Properties built in the 1960s')
    plt.show()

    print('Compare the median and mean of logerror:\n', train.logerror.mean(), train.logerror.median())

def ttest_hypo(train):
    '''
    This function prints the hypothesis testing for the T-test.
    '''
    alpha = 0.05
    prop_1960s = train[train.decade == 196.00]

    t, p = stats.ttest_1samp(prop_1960s.logerror, train.logerror.mean())

    print(f't = {t:.3f}')
    print(f'p = {p:.3f}')

    null_hypothesis = 'there is no difference in Zestimate log error in properties built in the 1950s and the overall log error.'

    if p < alpha:
        print("We reject the hypothesis that", null_hypothesis)
    else:
        print("We fail to reject the null hypothesis.")

def make_is_1960s(train):
    train['is_1960s'] = train.decade == 196.00
    train.is_1960s = train.is_1960s.map({False: 0, True: 1})
    return train

def error_heatmap(train):
    # pandas pivot
    heatmap1_data = pd.pivot_table(train, values='logerror', 
                        index=pd.cut(train['yearbuilt'], bins=6, precision=0), 
                        columns='county')
    heatmap1_data.sort_index(inplace=True, ascending=False)
    sns.heatmap(heatmap1_data, cmap="RdPu", square=True, annot=True)
    plt.title('Which properties have more log error, by year built bins and county?')
    plt.show

def map_1960s(train):
    sns.scatterplot(x='longitude', y='latitude', hue='is_1960s', data=train.drop(columns=['logerror']))
    plt.title("Where are the properties built in the 1960s located?")
    plt.show()

def bath_plot(train):
    sns.boxplot(x="bathcnt", y="logerror", data=train)
    plt.xlabel("Bathrooms")
    plt.ylabel("Log error")
    plt.title("Is there a relationship between\nbathroom count\nand log error?\n")
    plt.show()

def prop_val_log_plot(train):
    sns.jointplot(x="logerror", y="value", data=train)
    plt.xlabel("Property Value")
    plt.ylabel("Log error")
    plt.title("Is there a relationship\nbetween property value and log error?\n")
    plt.show()

def county_log_plot(train):
    sns.violinplot(x="county", y="logerror", data=train)
    plt.xlabel("County")
    plt.ylabel("Log error")
    plt.title("Is there a relationship\nbetween county and log error?\n")
    plt.show()

def map_k(X, train):
    #X = train_scaled[['latitude', 'longitude', 'county']]
    n_clusters=4
    kmeans = KMeans(n_clusters, n_init=20).fit(X)

    fig, axs = plt.subplots(2, 2, figsize=(13, 13), sharex=True, sharey=True)
    # this is useful because with one of the originals feature, county, we only get 3 groups.
    # with kmeans clustering we can get more groups based on area.
    # it's also helpful to get a more even distribution of the data per area
    for ax, k in zip(axs.ravel(), range(3, 7)):
        clusters = KMeans(k).fit(X).predict(X)
        ax.scatter(X.longitude, X.latitude, c=clusters)
        ax.set(title='k = {}'.format(k), xlabel='longitude', ylabel='latitude')

def cluster_log_plot(train):
    sns.jointplot(x="cluster_area", y="logerror", data=train)
    plt.xlabel("Area Clusters")
    plt.ylabel("Log error")
    plt.title("Is there a relationship between\narea cluster\nand log error?\n")
    plt.show()