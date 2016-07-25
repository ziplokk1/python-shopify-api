# Description

Contains wrappers and parsers for Shopify's Products API.

# Usage

```python
from shopify.products import ShopifyApiWrapper, Product, Image

api_key = '<api_key>'
password = '<password>'
store_name = '<store_name>'

saw = ShopifyApiWrapper(api_key, password, store_name)
for product in saw.list():
    print product.title
    
product = Product(title='My test product')
image = Image()
image.src = 'https://www.imageurl.com/myimage.jpg'
product.image = image
product.add_tags('testing', 'product')

product = saw.create(product)

product.title = 'My New Title For My Test Product'

saw.update(product)
```

# Installation

`pip install git+https://github.com/ziplokk1/python-shopify-api.git`