import unittest
import json

from app import create_app
from app.model import sales, products, Product


class TestSales(unittest.TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.sales = sales
        self.product = Product
        self.products = products
        self.product1 = self.product(1, "benwa", 5000)
        self.product2 = self.product(2, "meshu", 8000)
        self.products = [self.product1, self.product2]

    # Test cases for add sales record

    def test_create_sale(self):
        post_signup = dict(name="Fahad", price=12)
        response1 = self.app.post('/api/v1/products', json=post_signup)
        post_sale = dict(cart={"Fahad": 2})
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert "Sale of ID 1 has been created" == json.loads(response.data)['message']

    def test_empty_entries(self):
        post_sale = dict()
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        print(json.loads(response.data))
        assert "please fill missing fields" == json.loads(response.data)['message']

    def test_wrong_input(self):
        post_sale = dict(cart="mission")
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "please input correct format" in json.loads(response.data)['message']

    def test_product_not_found(self):
        post_sale = dict(cart={"finca": 2, "manny": 4})
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 404
        assert response.headers["Content-Type"] == "application/json"
        assert "['finca', 'manny'] products can not be found" == json.loads(response.data)['message']
