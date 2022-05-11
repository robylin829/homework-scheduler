from itsdangerous import exc
from app import db
from app.models import Schedules
from app.schemas.schedule_schema import *
from flask_restx import Resource, Namespace, fields

api = Namespace(
    'Schedule',
    description="Schedule API"
)

get_schedules_data = ('Model', {
    'id': fields.Integer(),
    'day': fields.String(),
    'lesson': fields.String(),
    'courses': fields.String()
})

create_schedules_data = ('Model', {
    'day': fields.String(),
    'lesson': fields.String(),
    'courses': fields.String(),
    'class_num': fields.Integer()
})

@api.route('/')
class SchedulesAPI(Resource):
    @api.marshal_with(get_schedules_data)
    def get(self):
        schedules = Schedules.query.order_by(Schedules.day).order_by(Schedules.lesson).all()
        schedules_output = schedules_schema.dump(schedules)
        return schedules_output

    @api.expect(create_schedules_data)
    def post(self):
        data = api.payload
        try:
            schedule = Schedules(
                day = data['day'],
                lesson = data['lesson'],
                courses = data['courses'],
                class_num = data['class_num']
            )
        except:
            return {'message': 'Miss something'}
        db.session.add(schedule)
        db.session.commit()
        return {'message': 'Created success'}

@api.route('/<int:id>')
class ScheduleAPI(Resource):
    def getSchedule(self, id):
        return Schedules.query.filter_by(id=id)

    @api.marshal_with(get_schedules_data)
    def get(self, id):
        schedule = self.getSchedule(id)
        schedule_output = schedule_schema.dump(schedule)
        return schedule_output
    
    @api.expect(create_schedules_data)
    def put(self, id):
        data = api.payload
        schedule = self.getSchedule(id)
        try:
            schedule.day = data['day']
            schedule.lesson = data['lesson']
            schedule.courses = data['courses']
            schedule.class_num = data['class_num']
        except:
            return {'message': 'Modified failure'}
        return {'message': 'Modified success'}

    def delete(self, id):
        schedule = self.getSchedule(id)
        if schedule == None:
            return {'message': 'Find nothing'}
        db.session.delete(schedule)
        db.sesison.commit()
        return {'message': 'Deleted success'}