##### Preparation file for store/items dataset and OPS datasets for Codeup Time series exercise:


#####IMPORTS#########################
import pandas as pd
from datetime import timedelta, datetime
import numpy as np

######## SALES/ITEMS DATASET ################

"""Function to change sales_date to data/time format and set as df index"""
def date_time_index(df):
    #set sale_date to be date and time format
    df.sale_date=pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')

    #Reset sale_date to be index:
    df = df.set_index("sale_date").sort_index()
    return df

"""Function to add month/day of week and sales_total columns"""
def add_columns(df):
    df['month']= df.index.strftime('%m-%b')
    df['day_of_week']= df.index.strftime('%A')
    df['sales_total']= df.sale_amount + df.item_price

    return df

#combining all the above:
def prep_storeitems():
    df = date_time_index(df)
    df = add_columns(df)
    return df

########## OPS DATASET ########################
"""Function to create date/time format and Date as index"""
def ops_datetime_index(df):
    df.Date=pd.to_datetime(df.Date)
    #set as index
    df = df.set_index("Date").sort_index()
    return df

"""Function to add month/year columns"""

def add_ops_columns(df):
    #adding month column
    df['month']= df.index.strftime('%m-%b')

    #adding year column
    df['year']=df.index.strftime('%Y')
    return df

"""Function to fillna with 0 for nulls"""

def fill_nulls(df):
    df = df.fillna(0)
    return df

#combining all of the above:
def prep_ops():
    df = ops_datetime_index(df)
    df = add_ops_columns(df)
    df = fill_nulls(df)
    return df