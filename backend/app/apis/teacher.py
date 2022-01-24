from app import db
from app.models import Teachers
from app.schemas.teacher_schema import *
from flask_restx import Resource, Namespace, fields

api = Namespace(
    'Teacher',
    description="Teacher api"
)

get_teachers_data = api.model('Model', {
    'id': fields.Integer(),
    'name': fields.String(),
    'course_id': fields.Integer()
})

create_teacher_data = api.model('Model', {
    'name': fields.String(),
    'course_id': fields.Integer()
})

@api.route('/')
class TeachersAPI(Resource):
    @api.marshal_with(get_teachers_data)
    def get(self):
        teacher = Teachers.query.order_by(Teachers.id).all()
        teacher_output = teachers_schema.dump(teacher)
        print(teacher_output)
        return teacher_output

    @api.expect(create_teacher_data)
    def post(self):
        data = api.payload
        teacher = Teachers(
            name = data['name'],
            course_id = data['course_id']
        )
        try:
            db.session.add(teacher)
            db.session.commit()
        except:
            return {'message': 'Created failure'}
        return {'message': 'Created success'}

@api.route('/<int:id>')
class TeacherAPI(Resource):
    def getTeacher(self, id):
        return Teachers.query.filter_by(id=id)

    @api.marshal_with(get_teachers_data)
    def get(self, id):
        try:
            teacher = self.getTeacher(id)
        except:
            return {'message': 'Find nothing'}
        teacher_output = teacher_schema.dump(teacher)
        return teacher_output
    
    @api.expect(create_teacher_data)
    def put(self, id):
        data = api.payload
        try:
            teacher = self.getTeacher(id)
        except:
            return {'message': 'Find nothing'}
        teacher.name = data['name']
        teacher.course_id = data['course_id']
        db.session.add(teacher)
        db.session.commit()
        return {'message': 'Modified success'}

    def delete(self, id):
        try:
            teacher = self.getTeacher(id)
        except:
            return {'message': 'Find nothing'}
        db.sessoin.delete(teacher)
        db.session.commit()
        return {'message': 'Deleted success'}