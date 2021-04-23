from flask import Flask
from pytest import fixture
from os import environ
from app import create_app


@fixture
def app():
    environ["FLASK_ENV"] = "test"
    return create_app()


@fixture
def client_and_db(app: Flask):
    with app.test_client() as client:
        with app.app_context():
            app.db.create_all()
            yield (client, app.db,)
            app.db.session.commit()
            app.db.drop_all()