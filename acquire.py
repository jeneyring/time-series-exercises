import pandas as pd
import requests
import os

def get_payload_data():
    filename = "payload.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        return combine_df(df)


def get_items():
    items = requests.get('https://python.zgulde.net/api/v1/items')
    #clarify to make as a json
    items = items.json()
    #create items from payloads into df
    items=pd.DataFrame(items['payload']['items'])
    return items

def get_stores():
    stores = requests.get('https://python.zgulde.net/api/v1/stores')
    stores = stores.json()
    stores=pd.DataFrame(stores['payload']['stores'])
    return stores

def get_sales():
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    #the name of my lists I want to store things in:
    sales = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        # .extend adds elemnts from a list to another list
        sales.extend(data['payload']['sales'])
        endpoint = data['payload']['next_page']
        print (endpoint)

        return sales = pd.DataFrame(sales)

def combine_df(df):
    df = get_payload_data()
    df = get_items()
    df = get_stores()
    df = get_sales()
    return df


