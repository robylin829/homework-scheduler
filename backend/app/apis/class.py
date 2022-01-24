from app import db
from app.models import Classes
from app.schemas.class_schema import *
from flask_restx import Resource, Namespace, fields

api = Namespace(
    'Class',
    description='Class API'
)

get_classes_data = api.model('Model', {
    
})