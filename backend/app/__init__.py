from flask import Flask

def create_app():
    app = Flask(__name__)

    from .apis import blueprint as api
    app.register_blueprint(api)

    return app