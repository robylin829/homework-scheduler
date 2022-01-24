from app import ma
from app.models import Courses

class CoursesShcema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Courses

course_schema = CoursesShcema()
courses_shcema = CoursesShcema(many=True)