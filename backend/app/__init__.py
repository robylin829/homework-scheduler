from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configs import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    db.init_app(app)

    # Api blueprint
    from .apis import blueprint as api
    app.register_blueprint(api, url_prefix="/api/v1")
    
    return app