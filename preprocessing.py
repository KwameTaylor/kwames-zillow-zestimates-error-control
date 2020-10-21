import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, explained_variance_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, TweedieRegressor
from sklearn.ensemble import IsolationForest
from sklearn.feature_selection import RFE

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

def isolation_forest(X_train, X_validate, X_test, y_train, y_validate, y_test):
    # Isolation Forest
    # identify outliers in the each dataset and train the models
    iso = IsolationForest(max_samples=100, random_state=666, contamination=0.3)
    yhat = iso.fit_predict(X_train)

    iso_v = IsolationForest(max_samples=100, random_state=666, contamination=0.3)
    yhat_v = iso.fit_predict(X_validate)

    iso_t = IsolationForest(max_samples=100, random_state=666, contamination=0.3)
    yhat_t = iso.fit_predict(X_test)

    # select all rows that are not outliers
    mask = yhat != -1
    X_train, y_train = X_train[mask], y_train[mask]

    mask = yhat_v != -1
    X_validate, y_validate = X_validate[mask], y_validate[mask]

    mask = yhat_t != -1
    X_test, y_test = X_test[mask], y_test[mask]

    # summarize the shape of the updated training dataset
    print('New shapes of train data:', X_train.shape, y_train.shape)
    # fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # evaluate the model
    yhat = model.predict(X_validate)
    # evaluate predictions
    mae = mean_absolute_error(y_validate, yhat)
    print('Mean Absolute error on validate data: %.3f' % mae)

    return X_train, X_validate, X_test, y_train, y_validate, y_test

def concat_dfs(train, X_train, y_train):
    train = X_train
    train['logerror'] = y_train
    print('Shape:', train.shape)
    return train

def my_RFE(X, k, train_scaled):
    # create and fit linear regression object
    lm = LinearRegression(normalize = True)
    lm.fit(X, train_scaled.logerror)
    # create and fit the rfe object
    rfe = RFE(lm, k)
    rfe.fit(X, train_scaled.logerror)
    X.columns[rfe.support_]

    print(rfe.support_)

    print('\nRFE Selected Features:\n', X.columns[rfe.support_])