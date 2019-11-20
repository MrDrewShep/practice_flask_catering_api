import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']


class Development(Config):
    DEBUG = True


class Production(Config):
    pass


class Testing(Config):
    TESTING = True


