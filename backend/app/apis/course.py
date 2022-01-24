from flask_restx import Resource, Namespace, fields
from app.models import Courses
from app.schemas.course_shcema import * 
from app import db

api = Namespace(
    'course',
    discription="Add Course"
)

get_course_data = api.model('Model', {
    'course_name': fields.String(),
})

@api.route('/get')
class GetCourse(Resource):
    @api.marshal_with(get_course_data)
    def get(self):
        courses = Courses.query.order_by(Courses.id).all()
        courses_output = courses_shcema.dump(courses)
        return courses_output

create_course_data = api.model('Model', {
    'course_name': fields.String()
})

@api.route('/create')
class CreateCourse(Resource):
    @api.expect(create_course_data)
    def post(self):
        data = api.payload
        print(data)
        course = Courses(course_name=data['course_name'])
        db.session.add(course)
        db.session.commit()
        return data