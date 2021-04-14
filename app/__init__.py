from flask import Flask
from app.configurations import database, migration
from app import views
import config


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    return app