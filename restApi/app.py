import pandas as pd 
import requests as rq



base_url = 'https://fakestoreapi.com'

#function that fetches the data 
def fetch(endpoint):
    url = f'{base_url}/{endpoint}'
    response = rq.get(url)
    response.raise_for_status()
    return response.json()

#fetch  multiple endpoints 
products = fetch('products')
users = fetch('users')
carts = fetch('carts')
categories = fetch('products/categories')

#data formating 
products_df = pd.DataFrame(products)
users_df = pd.DataFrame(users)
carts_df = pd.DataFrame(carts)
categories_df = pd.DataFrame(categories, columns= ['category_name'])

#show previews
print(products_df.head())
print(users_df.head())
print(carts_df.head())
print(categories_df.head())


df_carts_exploded = carts_df.explode('products')
carts_products = pd.json_normalize(df_carts_exploded['products'])

