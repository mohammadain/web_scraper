import pandas as pd
from brand_analysis import *

try:
    brands_data = []

    # Reading data from json
    # File should exist on root
    df = pd.read_json('products.json')

    # Getting unique brands
    brands = df['brand'].unique()

    # Iterate through the brands to get brand's maximum product price,
    # brand's minimum product price and brand's average price
    for brand in brands:
        brand_analysis = BrandAnalysis()
        brand_products = df.loc[df['brand'] == brand]
        max_price_product = brand_products.loc[brand_products['price'].idxmax()]
        min_price_product = brand_products.loc[brand_products['price'].idxmin()]
        avg_price_product = brand_products['price'].mean()

        brand_analysis.brand_name = brand
        brand_analysis.max_price_prod_name = max_price_product['name']
        brand_analysis.max_price = max_price_product['price']
        brand_analysis.max_price_prod_url = max_price_product['url']
        brand_analysis.min_price_prod_name = min_price_product['name']
        brand_analysis.min_price = min_price_product['price']
        brand_analysis.min_price_prod_url = min_price_product['url']
        brand_analysis.brand_avg_price = avg_price_product

        brands_data.append(brand_analysis)

    for brand in brands_data:

        print(brand.brand_name)
        print('Maximum price product: ' + brand.max_price_prod_name + ', ' + str(brand.max_price) + ', '
              + brand.max_price_prod_url)
        print('Minimum price product: ' + brand.min_price_prod_name + ', ' + str(brand.min_price) + ', '
              + brand.min_price_prod_url)
        print('Average price: ' + str(round(brand.brand_avg_price, 2)))
        print('\n')

# handle all the errors here
except Exception as e:
    print("An exception occurred " + str(e))


