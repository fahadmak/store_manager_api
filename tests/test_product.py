import unittest
from app import create_app
from app.model import products


class TestProductApi(unittest.TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.products = products

    def test_add_products(self):
        post_signup = dict(name="Fahad", price=12)
        response = self.app.post('/api/v1/products', json=post_signup)
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert "Fahad" in str(response.data)
        assert "Fahad" in [product.name for product in self.products]

    def test_empty_fields(self):
        post_signup = dict(name="Fahad")
        response = self.app.post('/api/v1/products', json=post_signup)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "missing fields" in str(response.data)

