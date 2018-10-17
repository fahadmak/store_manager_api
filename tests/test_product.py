import unittest
from app import create_app
from app.model import products


class TestProductApi(unittest.TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.products = products

    # Test cases for add products

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

    def test_incorrect_input(self):
        post_signup = dict(name=1, price=1)
        response = self.app.post('/api/v1/products', json=post_signup)
        # assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "incorrect information" in str(response.data)

    def test_user_already_exists(self):
        post_signup = dict(name="Fahad", price=12)
        post_signup2 = dict(name="Fahad", price=12)
        response = self.app.post('/api/v1/products', json=post_signup)
        response2 = self.app.post('/api/v1/products', json=post_signup2)
        assert response2.status_code == 409
        assert response2.headers["Content-Type"] == "application/json"
        assert "Fahad already exists" in str(response2.data)

    # Tests for get all products

    def test_get_all_products(self):
        post_signup = dict(name="Fahad", price=12)
        post_signup2 = dict(name="Jowe", price=120)
        response = self.app.post('/api/v1/products', json=post_signup)
        response2 = self.app.post('/api/v1/products', json=post_signup2)
        response3 = self.app.get('/api/v1/products')
        assert response3.status_code == 200
        assert response3.headers["Content-Type"] == "application/json"
        assert "Fahad" and "Jowe" in str(response3.data)

