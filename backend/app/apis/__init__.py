from flask import Blueprint
from flask_restx import Api, Namespace

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title="API",
    version="1.0",
    doc="/docs"
)

# Api factory
api.add_namespace()