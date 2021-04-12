from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.barber_shop_model import Barber_shop
    from app.models.address import Address
    from app.models.barbers import Barbers
    from app.models.client import Client
    from app.models.services import Services