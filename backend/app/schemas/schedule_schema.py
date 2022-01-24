from app import ma
from app.models import Schedules

class SchedulesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Schedules

schedule_schema = SchedulesSchema()
schedules_schema = SchedulesSchema(many=True)