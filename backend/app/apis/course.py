from flask_restx import Resource, Namespace, fields
from app.models import Courses
from app.schemas.course_shcema import * 
from app import db

api = Namespace(
    'course',
    discription="Add Course"
)

get_course_data = api.model('Model', {
    'id': fields.Integer(),
    'course_name': fields.String(),
})

create_course_data = api.model('Model', {
    'course_name': fields.String()
})

@api.route('/')
class CoursesAPI(Resource):
    @api.marshal_with(get_course_data)
    def get(self):
        courses = Courses.query.order_by(Courses.id).all()
        courses_output = courses_shcema.dump(courses)
        return courses_output

    @api.expect(create_course_data)
    def post(self):
        data = api.payload
        print(data)
        course = Courses(course_name=data['course_name'])
        db.session.add(course)
        db.session.commit()
        return data

@api.route('/<int:id>')
class CourseAPI(Resource):
    def getCourses(self, id):
        return Courses.query.filter_by(id=id).first()

    def get(self, id):
        course = self.getCourses(id)
        course_ouput = course_schema.dump(course)
        return course_ouput

    def delete(self, id):
        course = self.getCourses(id)
        db.session.delete(course)
        db.session.commit()
        return {"message": "Delete Success"}

    @api.expect(get_course_data)
    def put(self, id):
        data = api.payload
        course = self.getCourses(id)
        course.course_name = data['course_name']
        db.session.add(course)
        db.session.commit()