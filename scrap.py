# Import libraries
import requests
import time
import json
from bs4 import BeautifulSoup
from product import *

try:
    products = []
    url = 'https://www.fenom.com/en/263-men'

    products_per_page = 48
    products_to_fetch = 300
    pages_to_visit = int(products_to_fetch / products_per_page) + (products_to_fetch % products_per_page > 0)

    for page in range(pages_to_visit):

        page_url = url + '?p=' + str(page + 1)

        headers = {'User-Agent'
                   : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}

        # Connect to the URL
        product_listing_response = requests.get(page_url, headers=headers)

        # Parse HTML and save to BeautifulSoup object
        product_listing = BeautifulSoup(product_listing_response.text, "html.parser")

        # Iterate over the each product
        for a in product_listing.select("#product_list .right-block a"):

            product = Product()
            categories = []
            sizes = []
            description = []
            image_urls = []
            product_url = a['href']
            product.url = product_url
            single_product_response = requests.get(product_url, headers=headers)
            single_product = BeautifulSoup(single_product_response.text, "html.parser")

            # Setting values for
            # product name, product category, product price, product price currency code,
            # product brand, product image urls
            single_product_content = single_product.select('.nosto_product span')
            if single_product_content:
                for product_attrs in single_product_content:
                    product_attrs_class = product_attrs.get('class')[0]
                    if product_attrs_class == 'name':
                        product.name = product_attrs.text
                    elif product_attrs_class == 'category':
                        categories.append(product_attrs.text.split('/')[-1])
                        product.categories = categories
                    elif product_attrs_class == 'price':
                        product.price = product_attrs.text
                    elif product_attrs_class == 'price_currency_code':
                        product.currency = product_attrs.text
                    elif product_attrs_class == 'brand':
                        product.brand = product_attrs.text
                    elif product_attrs_class == 'alternate_image_url':
                        image_urls.append(product_attrs.text)
                        product.image_urls = image_urls

            # Setting values for product sizes
            single_product_sizes = single_product.select('.box-info-product .size_EU')
            if single_product_sizes:
                for size in single_product_sizes:
                    sizes.append(size.text)
                product.sizes = sizes

            # Setting value for product previous price
            product_previous_price = single_product.select_one('#old_price_display .price').text
            if product_previous_price:
                product.previous_price = product_previous_price
            else:
                del product.previous_price

            # Setting value for product reference label
            single_product_ref_label = single_product.select_one('#product_reference label')
            if single_product_ref_label:
                description.append(single_product_ref_label.text.replace(' ',''))

            # Setting value for product reference
            single_product_ref = single_product.select_one('#product_reference span')
            if single_product_ref:
                description.append(single_product_ref.text)

            # Setting values for product description
            single_product_des = single_product.select('#short_description_content p')
            if single_product_des:
                for des in single_product_des:
                    description.append(des.text[2:])
                product.description = description

            time.sleep(3)
            products.append(dict(product))

    print('Products successfully scraped...')

    # File will be placed on project root with name "products.json"
    with open('products.json', 'w') as outfile:
        json.dump(products, outfile, indent=4)

# handle all the errors here
except Exception as e:
    print("An exception occurred " + str(e))