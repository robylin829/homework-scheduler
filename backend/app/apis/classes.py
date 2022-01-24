from msilib.schema import Class
from app import db
from app.models import Classes
from app.schemas.class_schema import *
from flask_restx import Resource, Namespace, fields

api = Namespace(
    'Class',
    description='Class API'
)

get_classes_data = api.model('Model', {
    'id': fields.Integer(),
    'class_num': fields.String(),
    'schedules': fields.String()
})

create_classes_data = api.model('Model', {
    'class_num': fields.String(),
    'schedules': fields.String()
})

@api.route('')
class ClassesAPI(Resource):
    @api.marshal_with(get_classes_data)
    def get(self):
        classes = Classes.query.order_by(Classes.class_num).all()
        classes_output = classes_schema.dump(classes)
        return classes_output
    @api.expect(create_classes_data)
    def post(self):
        data = api.payload
        try:
            classes = Classes(
                class_num=data['class_num'],
                schedules=data['schedules']
            )
            db.session.add(classes)
            db.session.commit()
        except:
            return {'message': 'The class may already exist'}
        return {'message': 'Created success'}

@api.route('/<int:id>')
class ClassAPI(Resource):
    def getClass(self, id):
        return Classes.query.filter_by(id=id).first()

    @api.marshal_with(get_classes_data)
    def get(self, id):
        classes = self.getClass(id)
        classes_output = class_schema.dump(classes)
        return classes_output

    @api.expect(create_classes_data)
    def put(self, id):
        data = api.payload
        classes = self.getClass(id)
        try:
            classes.class_num = data['class_num']
            classes.schedules = data['schedules']
        except:
            return {'message': 'Modified failure'}
        return {'message': 'Modified success'}
    
    def delete(self, id):
        classes = self.getClass(id)
        if classes == None:
            return {'message': 'Find nothing'}
        db.session.delete(classes)
        db.session.commit()
        return {'message': 'Deleted success'}