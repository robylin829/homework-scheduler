from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
admin = Admin(name='Admin', template_mode='bootstrap4')

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    admin.init_app(app)
    CORS(app)
    
    with app.app_context():
        db.create_all()

    # Flask-Admin setting
    from flask_admin.contrib.sqla import ModelView
    from app.models import Schedules, Courses, Teachers, Classes
    admin.add_view(ModelView(Schedules, db.session))
    admin.add_view(ModelView(Courses, db.session))
    admin.add_view(ModelView(Teachers, db.session))
    admin.add_view(ModelView(Classes, db.session))

    # Api blueprint
    from .apis import blueprint as api
    app.register_blueprint(api, url_prefix='/api/v1')
    
    return app