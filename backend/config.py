from secrets import token_urlsafe

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = token_urlsafe(30)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

configs = {
    'development': DevConfig,
    'production': ProConfig,
}