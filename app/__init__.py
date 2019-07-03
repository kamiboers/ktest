from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.views.base import base
    app.register_blueprint(base)

    return app
