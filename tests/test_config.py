import unittest
from app import create_app


class TestDevelopmentConfig(unittest.TestCase):

    def test_app_is_development(self):
        app = create_app("development")
        self.assertTrue(app.config['DEBUG'] is True)

    def test_app_is_testing(self):
        app = create_app("testing")
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

    def test_app_is_production(self):
        app = create_app("production")
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['TESTING'] is False)

