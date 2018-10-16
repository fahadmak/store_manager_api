from flask import Flask
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from .user.view import user as user_blueprint
    app.register_blueprint(user_blueprint)
    return app


app = create_app("development")

