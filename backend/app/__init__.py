from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from app.configs import config

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name="Admin", template_mode="bootstrap4")

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    # Flask-Admin setting
    from flask_admin.contrib.sqla import ModelView
    from app.models import Schedules, Courses, Teachers
    admin.add_view(ModelView(Schedules, db.session))
    admin.add_view(ModelView(Courses, db.session))
    admin.add_view(ModelView(Teachers, db.session))

    # Api blueprint
    from .apis import blueprint as api
    app.register_blueprint(api, url_prefix="/api/v1")
    
    return app