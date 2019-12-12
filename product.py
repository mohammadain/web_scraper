class Product:

    def __init__(self):
        self.__name = ''
        self.__url = ''
        self.__categories = []
        self.__price = 0.0
        self.__previous_price = 0.0
        self.__currency = ''
        self.__sizes = []
        self.__description = []
        self.__image_urls = []
        self.__brand = ''

    # using property decorator

    # name getter function
    @property
    def name(self):
        return self.__name

    # name setter function
    @name.setter
    def name(self, value):
        self.__name = value

    # url getter function
    @property
    def url(self):
        return self.__url

    # url setter function
    @url.setter
    def url(self, value):
        self.__url = value

    # categories getter function
    @property
    def categories(self):
        return self.__categories

    # categories setter function
    @categories.setter
    def categories(self, value):
        self.__categories = value

    # price getter function
    @property
    def price(self):
        return self.__price

    # price setter function
    @price.setter
    def price(self, value):
        self.__price = value

    # previous_price getter function
    @property
    def previous_price(self):
        return self.__previous_price

    # previous_price setter function
    @previous_price.setter
    def previous_price(self, value):
        self.__previous_price = value

    # previous_price deleter function
    @previous_price.deleter
    def previous_price(self):
        del self.__previous_price

    # currency getter function
    @property
    def currency(self):
        return self.__currency

    # currency setter function
    @currency.setter
    def currency(self, value):
        self.__currency = value

    # sizes getter function
    @property
    def sizes(self):
        return self.__sizes

    # sizes setter function
    @sizes.setter
    def sizes(self, value):
        self.__sizes = value

    # description getter function
    @property
    def description(self):
        return self.__description

    # description setter function
    @description.setter
    def description(self, value):
        self.__description = value

    # image_urls getter function
    @property
    def image_urls(self):
        return self.__image_urls

    # image_urls setter function
    @image_urls.setter
    def image_urls(self, value):
        self.__image_urls = value

    # brand getter function
    @property
    def brand(self):
        return self.__brand

    # brand setter function
    @brand.setter
    def brand(self, value):
        self.__brand = value

    def __iter__(self):
        yield 'name', self.name
        yield 'url', self.url
        yield 'categories', self.categories
        yield 'price', self.price
        if hasattr(self, 'previous_price'):
            yield 'previous_price', self.previous_price
        yield 'currency', self.currency
        yield 'sizes', self.sizes
        yield 'description', self.description
        yield 'image_urls' , self.image_urls
        yield 'brand', self.brand