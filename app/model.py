products = []
sales = []


class Product:
    """
        A class used to represent a Product

        ...

        Attributes
        ----------
        name : str
            the name of the product
        price : str
            the price of the product

        Methods
        -------
        to_json(self)
            Converts the product instance to a dictionary
    """
    def __init__(self, productId, name, price):
        self.productId = productId
        self.name = name
        self.price = price

    def __repr__(self):
        """A method to returns the string representation of an object"""
        return f"Product: {self.name} of ID {self.productId} has been added to inventory"

    def to_json(self):
        """A method to Convert the product instance to a dictionary"""
        product = {
            'productId': self.productId,
            'name': self.name,
            'price': self.price
        }
        return product


class Sale:
    """
        A class used to represent a Sale

        ...

        Attributes
        ----------
        saleId : int
            the id of the sale record
        cart : dict
            the products and there respective quantities
        date : str
            the time and date when sale record was created
        Methods
        -------
        to_json(self)
            Converts the sales instance to a dictionary
    """

    def __init__(self, saleId, cart, date):
        self.saleId = saleId
        self.cart = cart
        self.date = date

    def to_json(self):
        sale = {
            "saleId": self.saleId,
            "cart": self.cart,
            "date": self.date,
        }
        return sale