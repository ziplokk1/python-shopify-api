# coding: utf-8
"""
This example shows how to create new products via API
reading from a list of dictionaries containing products and
variants. 
__author__ = Bruno Rocha <rochacbruno@gmail.com> - brunorocha.org
"""

# REQUIREMENTS
# pip install slugify
# pip install python-shopify

import os
from slugify import slugify
from shopify.products import (
    ProductsApiWrapper, Product, Image, Variant, Option
)


# FILL THE DATA below
api_key = ''  
password = '' 
store_name = ''

paw = ProductsApiWrapper(api_key, password, store_name)

# Get a list of existing products, limited to 250 :(
existing = [item.title for item in paw.list(limit=250)]


def create_product(items):
    """Items is a list of dictionaries representing each product variant
    of the same product with the same ID and other data
    keys: ['description', 'price', 'name', 'link', 'size', 'stock']
    items = [
        # first variant holds full data and is default
        {'name': 'Awesome t-shirt', 
         'code': '123456', 
         'description': '<html>', 
         'size': 'P', 
         'price': '22.5',
         'stock': 2},
        # Other variants 
        {'size': 'M', 
         'price': '25.5',
         'stock': 2},
        {'size': 'G', 
         'price': '29.5',
         'stock': 0},
    ]
    """
    
    # The first item should be the complete item holding all the fields
    # other items can have only the variants
    data = items[0]

    # Use data['name'].decode('utf-8') if you are reading csv files
    name = data['name']  


    if name in existing or paw.list(title=name):
        # skip existing
        print "Already registered, skipping..."
        return

    product = Product(
        title=data['name'],
        body_html=data['description'],    
    )

    # There should be a 123456.jpg file in the same folder
    # alternatively you can use a URL provided in data
    image_filename = "{0}.jpg".format(data['code'])
    if os.path.exists(image_filename):
        image = Image()
        image.attach(image_filename)
        product.add_image(image)
    elif data.get('image_url'):
        product.add_image(Image(src=data['image_url']))

    # using the first word in title as tag
    # Product "T-shirt Blue 09" got tag "t-shirt"
    tag = data['name'].split()[0]
    tag = u''.join(i for i in tag if not i.isdigit())

    product.add_tags(tag.strip().lower())

    # You can add only 3 options
    # at positions 1, 2 and 3
    # you should add options before adding its variants
    product.add_option(
      Option(
        name="Size",
        position=1,
      )
    )
    
    for item in items:
        product.add_variant(
            Variant(
                option1=item['size'],
                # option2=data['size'],
                # option3=data['size'],
                title="Size",
                price=item['price'],
                # SKU should be different for each variant
                sku=data["code"] + slugify(item['size']), 
                position=1,
                inventory_policy="continue",
                fulfillment_service="manual",
                inventory_management="shopify",
                inventory_quantity=int(item['stock']),
                taxable=False,
                weight=300,
                weight_unit="g", # g, kg
                requires_shipping=True
            )
        )
    
    try:
        product = paw.create(product)
    except Exception as e:
        # do a proper logging here please!!!
        print e
        print product
        print items

    return product