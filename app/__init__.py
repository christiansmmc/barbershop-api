from flask import Flask
from app.configurations import flask_configuration, database, migration
from app import views


def create_app():
    app = Flask(__name__)

    flask_configuration.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    return app