from flask import Flask
from os import getenv
from datetime import timedelta


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = getenv("SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL_UPDATED")


class TestConfig(Config):
    ...


config_selector = {
    "development": DevelopmentConfig,
    "production": DevelopmentConfig,
    "test": TestConfig,
}


def init_app(app: Flask):
    config_type = getenv("FLASK_ENV")
    config_object = config_selector[config_type]
    app.config.from_object(config_object)