from objects import *
from api_wrapper import ProductsApiWrapper


def count(api_key, api_password, store_name):
    import json
    import requests

    url = 'https://{}:{}@{}.myshopify.com/admin/products/count.json'.format(api_key, api_password, store_name)
    response = requests.get(url)
    data = json.loads(response.content)
    return int(data['count'])
