from flask_marshmallow import Marshmallow
from flask import Flask


ma = Marshmallow()


def init_app(app: Flask):
    ma.init_app(app)