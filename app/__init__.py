from flask import Flask
from app.configurations import database, migration
from app import views
from flask_cors import CORS
import config


def create_app():
    app = Flask(__name__)
    CORS(app)

    config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    return app