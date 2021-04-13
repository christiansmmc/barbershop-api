from flask import Flask
<<<<<<< HEAD
from app.configurations import database, migration
from app import views
import config
=======
from app.configurations import flask_configuration, database, migration
from app import views
>>>>>>> f612008f0aea616b41a1a37af6b071dd42dd0416


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    
    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    views.init_app(app)

    return app