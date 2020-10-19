# import necessary packages/modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import sqrt

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

def corr_heatmap(X_train_scaled):
    '''
    This function creates a heatmap of the correlation of all features scaled, minus longitude and latitude.
    Takes a dataFrame as an argument
    '''
    # heatmap time!
    heatmap_data = X_train_scaled.drop(columns=['latitude', 'longitude'])
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
    alpha = 0.05
    prop_2000s = train[train.century == 20.00]

    sns.distplot(train.logerror)
    plt.title('Overall Log Error')
    #get rid of outliers on a later iteration
    plt.show()

    sns.distplot(prop_2000s.logerror)
    plt.title('Log Error of Properties built in the 2000s')
    plt.show()

    print('Compare the median and mean:\n', train.logerror.mean(), train.logerror.median())

def ttest_hypo(train):
    '''
    This function prints the hypothesis testing for the T-test.
    '''
    alpha = 0.05
    prop_2000s = train[train.century == 20.00]

    t, p = stats.ttest_1samp(prop_2000s.logerror, train.logerror.mean())

    print(f't = {t:.3f}')
    print(f'p = {p:.3f}')

    null_hypothesis = 'there is no difference in Zestimate log error in properties built in the 2000s and the overall log error.'

    if p < alpha:
        print("We reject the hypothesis that", null_hypothesis)
    else:
        print("We fail to reject the null hypothesis.")