from flask import Blueprint
from flask_restx import Api
from .courses import api as ns1
from .teachers import api as ns2
from .schedules import api as ns3
from .classes import api as ns4

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='API',
    version='1.0',
    doc='/docs'
)

# Api factory
api.add_namespace(ns1, path='/course')
api.add_namespace(ns2, path='/teacher')
api.add_namespace(ns3, path='/schedule')
api.add_namespace(ns4, path='/class')