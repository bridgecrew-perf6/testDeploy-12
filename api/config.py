import os
from decouple import config

class DevConfig:
    DEBUG=True

class TestConfig:
    TESTING=True

class ProdConfig:
    pass


config_dist = {
    'dev':DevConfig,
    'test':TestConfig,
    'prod':ProdConfig
}