from flask import Flask
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from .product.view import product as product_blueprint
    app.register_blueprint(product_blueprint)
    return app


