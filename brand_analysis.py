class BrandAnalysis:

    def __init__(self):
        self.__brand_name = ''
        self.__max_price_prod_name = 0.0
        self.__max_price = 0.0
        self.__max_price_prod_url = ''
        self.__min_price_prod_name = ''
        self.__min_price = 0.0
        self.__min_price_prod_url = ''
        self.__brand_avg_price = 0.0

    # using property decorator

    # brand_name getter function
    @property
    def brand_name(self):
        return self.__brand_name

    # brand_name setter function
    @brand_name.setter
    def brand_name(self, value):
        self.__brand_name = value

    # max_price_prod_name getter function
    @property
    def max_price_prod_name(self):
        return self.__max_price_prod_name

    # max_price_prod_name setter function
    @max_price_prod_name.setter
    def max_price_prod_name(self, value):
        self.__max_price_prod_name = value

    # max_price getter function
    @property
    def max_price(self):
        return self.__max_price

    # max_price setter function
    @max_price.setter
    def max_price(self, value):
        self.__max_price = value

    # max_price_prod_url getter function
    @property
    def max_price_prod_url(self):
        return self.__max_price_prod_url

    # max_price_prod_url setter function
    @max_price_prod_url.setter
    def max_price_prod_url(self, value):
        self.__max_price_prod_url = value

    # min_price_prod_name getter function
    @property
    def min_price_prod_name(self):
        return self.__min_price_prod_name

    # min_price_prod_name setter function
    @min_price_prod_name.setter
    def min_price_prod_name(self, value):
        self.__min_price_prod_name = value

    # min_price getter function
    @property
    def min_price(self):
        return self.__min_price

    # min_price setter function
    @min_price.setter
    def min_price(self, value):
        self.__min_price = value

    # min_price_prod_url getter function
    @property
    def min_price_prod_url(self):
        return self.__min_price_prod_url

    # min_price_prod_url setter function
    @min_price_prod_url.setter
    def min_price_prod_url(self, value):
        self.__min_price_prod_url = value

    # brand_avg_price getter function
    @property
    def brand_avg_price(self):
        return self.__brand_avg_price

    # brand_avg_price setter function
    @brand_avg_price.setter
    def brand_avg_price(self, value):
        self.__brand_avg_price = value