products = []
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
    def __init__(self, name, price):
        self.name = name
        self.price = price



