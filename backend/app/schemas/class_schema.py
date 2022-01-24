from app import ma
from app.models import Classes

class ClassesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Classes

class_schema = ClassesSchema()
classes_schema = ClassesSchema(many=True)