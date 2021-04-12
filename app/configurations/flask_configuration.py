from flask import Flask
from os import getenv

def init_app(app: Flask):
    # planejar user e db com grupo para configurar URI abaixo
    # app.config["SQLALCHEMY_DATABASE_URI"] = getenv("")  
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False