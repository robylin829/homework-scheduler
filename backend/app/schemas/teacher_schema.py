from app import ma
from app.models import Teachers

class TeachersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teachers

teacher_schema = TeachersSchema()
teachers_schema = TeachersSchema(many=True)