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

def zillow_scale(train, validate, test):
    '''
    This function takes in train, validate, test
    dataFrames, and returns them each in scaled form.
    '''
    scaler = MinMaxScaler().fit(train)
    train_scaled = (pd.DataFrame(scaler.transform(train), 
                      columns=train.columns, 
                      index=train.index))
    validate_scaled = (pd.DataFrame(scaler.transform(validate), 
                     columns=validate.columns,
                     index=validate.index))
    test_scaled = (pd.DataFrame(scaler.transform(test), 
                     columns=test.columns,
                     index=test.index))
    return scaler, train_scaled, validate_scaled, test_scaled

# note: encode county currently in wrangle, move here in future iteration
#def encode_county(df):
    # Encode County feature
    # I will map strings into 0s, 1s, and 2s:
    # 0 = Los Angeles County
    # 1 = Orange County
    # 2 = Ventura County
#    df.county = df.county.map({'Los Angeles': 0, 'Orange': 1, 'Ventura': 2})
#    return df

def handle_outliers(df):
    '''This function WILL handle outliers. Implementation in later iteration.
    '''
    return df