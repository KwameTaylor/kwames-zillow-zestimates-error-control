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
    This function acquires the Zillow property Zestimate data with a SQL query to the Codeup database.
    '''
    sql_query = '''
                SELECT * 
                FROM properties_2017
                JOIN predictions_2017 using(parcelid)
                LEFT JOIN airconditioningtype using(airconditioningtypeid)
                LEFT JOIN architecturalstyletype using(architecturalstyletypeid)
                LEFT JOIN buildingclasstype using(buildingclasstypeid)
                LEFT JOIN heatingorsystemtype using(heatingorsystemtypeid)
                LEFT JOIN propertylandusetype using(propertylandusetypeid)
                LEFT JOIN storytype using(storytypeid)
                LEFT JOIN typeconstructiontype using(typeconstructiontypeid)
                WHERE latitude IS NOT NULL
                AND longitude IS NOT NULL
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

def prepare_zillow(df):
    '''
    This function cleans up the Zillow property values data
    by reducing features.
    Returns df; takes df as argument.
    '''
    # Drop features to create an MVP (first iteration)

    # Just choosing features right now that sound unuseful to me to drop
    df = df.drop(columns=['calculatedbathnbr', 'roomcnt', 'assessmentyear', 'propertycountylandusecode', 'storytypeid', 'typeconstructiontypeid', 'buildingclasstypeid', 'architecturalstyletypeid', 'heatingorsystemtypeid', 'id', 'id.1', 'basementsqft', 'airconditioningtypeid', 'architecturalstyledesc', 'buildingclassdesc', 'heatingorsystemdesc', 'storydesc', 'typeconstructiondesc', 'censustractandblock', 'rawcensustractandblock', 'propertylandusetypeid'])

    # Drop redundant or unneeded square feet features
    df = df.drop(columns=['finishedfloor1squarefeet', 'finishedsquarefeet12', 'finishedsquarefeet13', 'finishedsquarefeet15', 'finishedsquarefeet50', 'finishedsquarefeet6', 'lotsizesquarefeet', 'garagetotalsqft', 'lotsizesquarefeet', 'yardbuildingsqft17', 'yardbuildingsqft26'])

    # Drop redundant or unneeded value and tax features
    df = df.drop(columns=['structuretaxvaluedollarcnt', 'landtaxvaluedollarcnt', 'taxamount', 'taxdelinquencyflag', 'taxdelinquencyyear'])

    # Drop more features based on how many nulls are present
    # I'll do it manually this iteration but might choose to automate later
    # (have to remember how much time I will save - or waste - with automation)
    df = df.drop(columns=['buildingqualitytypeid', 'decktypeid', 'fireplacecnt', 'hashottuborspa', 'poolsizesum', 'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'threequarterbathnbr', 'fireplaceflag'])

    # Drop features that could be useful in a later iteration but are just noise for the MVP
    df = df.drop(columns=['garagecarcnt', 'fullbathcnt', 'poolcnt', 'propertyzoningdesc', 'regionidcity', 'regionidneighborhood', 'numberofstories'])

    # Drop zip code related columns because zip codes are anonymized in this data
    df = df.drop(columns=['regionidzip'])

    # In next iteration of pipeline, I will turn transaction date into date type, but for now I will just drop that column.
    df = df.drop(columns=['transactiondate'])

    # In the next iteration of pipeline, I will impute airconditioningdesc and propertylandusedesc, and add the necessary documentation for that.
    # For now I will drop airconditioningdesc, and I will use propertylandusedesc to make sure I only have single-unit properties.
    df = df.drop(columns=['airconditioningdesc'])

    # Set index to parcelid to make it easier to drop rows and for better readability
    df = df.set_index('parcelid')

    # Now I will filter out all properties that are not single-unit properties.

    # Get names of indexes for non-Single Family Residental properties
    cols_to_drop = df[df['propertylandusedesc'] != 'Single Family Residential'].index
    # Delete these row indexes from dataFrame
    df = df.drop(cols_to_drop)

    # fillna on unitcnt with 1.00 and then drop rows that are not 1.00
    df.unitcnt = df.unitcnt.fillna(1.00)
    # Get names of indexes for non-Single Family Residental properties
    cols_to_drop = df[df['unitcnt'] != 1.00].index
    # Delete these row indexes from dataFrame
    df = df.drop(cols_to_drop)

    # Now to drop propertylandusedesc and unitcnt because I don't need them anymore
    df = df.drop(columns=['propertylandusedesc', 'unitcnt'])

    # Rename columns for readability
    df = df.rename(columns={"bathroomcnt": "bathcnt", "bedroomcnt": "bedcnt", "calculatedfinishedsquarefeet": "sqft", "regionidcounty": "county", "taxvaluedollarcnt": "value"})

    return df