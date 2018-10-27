import unittest
import json

from app import create_app
from app.models.model import sales, products, Product


class TestSales(unittest.TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.sales = sales
        self.product = Product
        self.products = products

    def test_sale_content_type(self):
        post_sale = dict(cart={"Fahad": 2})
        response = self.app.post('/api/v1/sales', json=post_sale, content_type='application/javascript')
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "Invalid content type" in str(response.data)

    # Test cases for add sales record

    def test_create_sale(self):
        post_signup = dict(name="Fahad", price=12, quantity=20)
        response1 = self.app.post('/api/v1/products', json=post_signup)
        print(post_signup['quantity'])
        post_sale = dict(cart={"Fahad": 2})
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert 18 in [product.quantity for product in self.products]
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert "Sale of ID 1 has been created" == json.loads(response.data)['message']

    def test_empty_entries(self):
        post_sale = dict()
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "please fill missing fields" == json.loads(response.data)['error']

    def test_wrong_input(self):
        post_sale = dict(cart="mission")
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "please input correct format" in json.loads(response.data)['error']

    def test_product_not_found(self):
        post_sale = dict(cart={"finca": 2, "manny": 4})
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "finca, manny can not be found" == json.loads(response.data)['error']

    def test_get_all_sales(self):
        post_signup = dict(name="Fahad", price=12, quantity=120)
        response1 = self.app.post('/api/v1/products', json=post_signup)
        post_sale = dict(cart={"Fahad": 2})
        response2 = self.app.post('/api/v1/sales', json=post_sale)
        response = self.app.get('/api/v1/sales')
        data = json.loads(response.data)['sales']
        assert isinstance(data, list)
        assert "total" in data[0]
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

    def test_no_sales(self):
        response = self.app.get('/api/v1/sales')
        data = json.loads(response.data)
        assert isinstance(data, dict)
        assert 'They are currently no sales' in data['error']
        assert response.status_code == 404
        assert response.headers["Content-Type"] == "application/json"

    def test_get_sale_by_id(self):
        post_signup = dict(name="Fahad", price=12, quantity=12)
        response1 = self.app.post('/api/v1/products', json=post_signup)
        post_sale = dict(cart={"Fahad": 2})
        response2 = self.app.post('/api/v1/sales', json=post_sale)
        response = self.app.get('/api/v1/sales/1')
        data = json.loads(response.data)['sale']
        assert "total" in data
        assert isinstance(data, dict)
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

    def test_sale_id_doesnot_exist(self):
        response = self.app.get('/api/v1/sales/1')
        data = json.loads(response.data)
        assert 'Sale Record of ID 1 does not exist' in data['error']
        assert isinstance(data, dict)
        assert response.status_code == 404
        assert response.headers["Content-Type"] == "application/json"

    def test_quantity_low_in_stock(self):
        post_signup = dict(name="Fahad", price=12, quantity=20)
        response1 = self.app.post('/api/v1/products', json=post_signup)
        print(post_signup['quantity'])
        post_sale = dict(cart={"Fahad": 200})
        response = self.app.post('/api/v1/sales', json=post_sale)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "Fahad these quantity are unavailable" == json.loads(response.data)['error']

    def tearDown(self):
        self.sales.clear()
