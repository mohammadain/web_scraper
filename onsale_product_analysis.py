import pandas as pd

try:
    onsale_product_count = {}

    # Reading data from json
    # File should exist on root
    df = pd.read_json('products.json')

    # Getting unique brands
    brands = df['brand'].unique()

    # Iterate through the brands to get each brands on sale products count
    for brand in brands:
        brand_products = df.loc[df['brand'] == brand]
        onsale_product_count[brand] = brand_products['previous_price'].value_counts().sum()

    for brand in onsale_product_count:
        print(brand + ': ' + str(onsale_product_count[brand]))

# handle all the errors here
except Exception as e:
    print("An exception occurred " + str(e))
