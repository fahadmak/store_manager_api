from flask import Flask
from config import app_config


def create_app(config_name):
    """create flask application and set dev environment"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from app.views.product import product as product_blueprint
    from app.views.sale import sale as sale_blueprint

    app.register_blueprint(product_blueprint)
    app.register_blueprint(sale_blueprint)

    return app
