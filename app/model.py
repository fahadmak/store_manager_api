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

    def __str__(self):
        return f"Product: {self.name}, has been added to inventory"

    def to_json(self):
        """A method to Convert the product instance to a dictionary"""
        product = {
            'name': self.name,
            'price': self.price
        }
        return product


