from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    # Api blueprint
    from .apis import blueprint as api
    app.register_blueprint(api)
    
    return app