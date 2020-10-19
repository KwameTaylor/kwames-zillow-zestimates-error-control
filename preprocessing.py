import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def zillow_main_split(df):
    '''
    This function takes in a DataFrame,
    performs a train, validate, test split,
    and returns the following:
    train, validate, test.
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

    return train, validate, test

def zillow_Xy_split(train, validate, test):
    '''
    This function takes in a DataFrame,
    performs an X and y train, X and y validate, X and y test split,
    and returns the following:
    X_train, X_validate, X_test, y_train, y_validate, y_test.
    '''

    X_train = train.drop(columns='logerror')
    X_validate = validate.drop(columns='logerror')
    X_test = test.drop(columns='logerror')

    y_train = train['logerror']
    y_validate = validate['logerror']
    y_test = test['logerror']

    return X_train, X_validate, X_test, y_train, y_validate, y_test

def impute_nulls(df):
    '''
    This function takes in a df,
    and imputes the median for columns
    sqft, yearbuilt, and value.
    '''
    # impute median for sqft
    df.sqft = df.sqft.fillna(df.sqft.median())
    # impute median for yearbuilt
    df.yearbuilt = df.yearbuilt.fillna(df.yearbuilt.median())
    # impute median for value
    df.value = df.value.fillna(df.value.median())
    return df

def zillow_scale(X_train, X_validate, X_test):
    '''
    This function takes in X_train, X_validate, X_test
    dataFrames, and returns them each in scaled form.
    '''
    scaler = MinMaxScaler().fit(X_train)
    X_train_scaled = (pd.DataFrame(scaler.transform(X_train), 
                      columns=X_train.columns, 
                      index=X_train.index))
    X_validate_scaled = (pd.DataFrame(scaler.transform(X_validate), 
                     columns=X_validate.columns,
                     index=X_validate.index))
    X_test_scaled = (pd.DataFrame(scaler.transform(X_test), 
                     columns=X_test.columns,
                     index=X_test.index))
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled