import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

import os

from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data():
    '''
    This function acquires the Zillow property values data with a SQL query to the Codeup database.
    '''
    sql_query = '''
                SELECT properties_2017.parcelid, properties_2017.id, bathroomcnt, bedroomcnt, calculatedbathnbr, calculatedfinishedsquarefeet, fips, latitude, longitude, regionidcounty, roomcnt, yearbuilt, taxvaluedollarcnt, assessmentyear, propertycountylandusecode, propertylandusetypeid
                FROM properties_2017
                JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid
                WHERE transactiondate BETWEEN '2017-05-01' AND '2017-06-30'
                AND propertylandusetypeid = '261' OR '262' OR '263' OR '264' OR '268' OR '273' OR '274' OR '275' OR '276' OR '279';
                '''
    filename = "zillow_df.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        #drop second index column
        df = df.drop(columns=['Unnamed: 0'])
        return df
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(sql_query, get_connection('zillow'))
        # Write the df to disk
        df.to_csv(filename)
        # Return the dataframe to the calling code
        return df

def prepare_zillow():
    '''
    This function acquires and prepares the Zillow property values data.
    Returns df; takes no arguments.
    '''
    df = get_zillow_data()

    # Drop features to create an MVP (first iteration)
    df = df.drop(columns=['calculatedbathnbr', 'fips', 'latitude', 'longitude', 'regionidcounty', 'roomcnt', 'yearbuilt', 'assessmentyear', 'propertycountylandusecode', 'propertylandusetypeid'])
    # Drop rows with NaNs
    df = df.dropna()

    return df