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

