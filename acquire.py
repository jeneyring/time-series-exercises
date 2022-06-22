#Acquiring datasets from API:

import pandas as pd
import requests
import os

def get_items():
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/items'
    items = []
    while True:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    items = pd.DataFrame(items)
    return items

def get_stores():
    response = requests.get('https://python.zgulde.net/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(stores['payload']['stores'])
    stores = pd.DataFrame(stores)
    return stores

def get_sales():
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    #the name of my lists I want to store things in:
    sales = []

    while True:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
        # .extend adds elemnts from a list to another list
        sales.extend(data['payload']['sales'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    sales = pd.DataFrame(sales)
    return sales 


def get_stores_data():
    if os.path.exists('stores.csv'):
        return pd.read_csv('stores.csv')
    df = get_stores()
    df.to_csv('stores.csv', index=False)
    return df

def get_items_data():
    if os.path.exists('items.csv'):
        return pd.read_csv('items.csv')
    df = get_items()
    df.to_csv('items.csv', index=False)
    return df

def get_sales_data():
    if os.path.exists('sales.csv'):
        return pd.read_csv('sales.csv')
    df = get_sales()
    df.to_csv('sales.csv', index=False)
    return df

def get_store_item_demand_data():
    sales = get_sales_data()
    stores = get_stores_data()
    items = get_items_data()

    sales = sales.rename(columns={'store': 'store_id', 'item': 'item_id'})
    df = pd.merge(sales, stores, how='inner', left_on='store_id', right_on='store_id')
    df = pd.merge(df, items, how='inner', left_on='item_id', right_on='item_id')
    return df

def get_opsd_data():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df