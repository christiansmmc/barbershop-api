from flask import Flask
from os import getenv


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")


class TestConfig(Config):
    ...


config_selector = {
    'development': DevelopmentConfig,
    'test': TestConfig,    
}


def init_app(app: Flask):
    config_type = getenv("FLASK_ENV")
    config_object = config_selector[config_type]
    app.config.from_object(config_object)