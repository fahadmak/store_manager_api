import unittest
from app.model import Product, products


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product
        self.products = products
        self.product1 = self.product(1, "benwa", 5000)
        self.products = [self.product1]

    def test_create_product(self):
        assert isinstance(self.product1, self.product)
        assert self.product1.name == "benwa"
        assert self.product1.price == 5000

    def test_to_json(self):
        product_json = self.product1.to_json()
        assert isinstance(product_json, dict)
        assert product_json == {"productId": 1, "name": "benwa", "price": 5000}


