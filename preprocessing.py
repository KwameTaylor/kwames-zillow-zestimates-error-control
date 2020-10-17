import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def zillow_split(df):
    '''
    This function takes in a DataFrame, performs a train, validate, test split,
    then an X and y train, validate, test split, and returns the following:
    train, validate, test, X_train, X_validate, X_test, y_train, y_validate, y_test.
    '''
    #Split the data
    train_validate, test = train_test_split(df, test_size=.2, random_state=666)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=666)

    X_train = train.drop(columns='logerror')
    X_validate = validate.drop(columns='logerror')
    X_test = test.drop(columns='logerror')

    y_train = train['logerror']
    y_validate = validate['logerror']
    y_test = test['logerror']

    return train, validate, test, X_train, X_validate, X_test, y_train, y_validate, y_test

def zillow_scale(df):
    '''
    This function WILL take in a DataFrame and return it in scaled form. Implementation on next MVP iteration.
    '''
    return df