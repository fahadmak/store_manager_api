from flask import Flask
from config import app_config


def create_app(config_name):
    """create flask application and set dev environment"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .product.view import product as product_blueprint
    from .sale.view import sale as sale_blueprint

    app.register_blueprint(product_blueprint)
    app.register_blueprint(sale_blueprint)

    return app

app = create_app("development")
