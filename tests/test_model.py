import unittest
from app.model import Product, products, Sale, sales


class TestModel(unittest.TestCase):
    def setUp(self):
        self.product = Product
        self.products = products
        self.product1 = self.product(1, "benwa", 5000)
        self.product2 = self.product(2, "meshu", 8000)
        self.products = [self.product1, self.product2]

        self.sale = Sale
        self.sales = sales
        self.sale1 = self.sale(1, {"benwa": 2, "meshu": 4})
        self.sales = [self.sale1]

    def test_create_product(self):
        assert isinstance(self.product1, self.product)
        assert self.product1.name == "benwa"
        assert self.product1.price == 5000

    def test_product_to_json(self):
        product_json = self.product1.to_json()
        assert isinstance(product_json, dict)
        assert product_json == {"productId": 1, "name": "benwa", "price": 5000}

    def test_create_sale(self):
        assert isinstance(self.sale1, self.sale)
        assert "benwa" in self.sale1.cart

    def test_sale_to_json(self):
        sale_json = self.sale1.to_json()
        assert isinstance(sale_json, dict)
