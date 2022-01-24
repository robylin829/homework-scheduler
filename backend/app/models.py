from app import db

# Schedule - course - teacher

# Each classes' schedule
class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # When is the course
    day = db.Column(db.String(20), nullable=False)
    lesson = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Courses', backref='schedules')
    classes_num = db.Column(db.Integer, db.ForeignKey('classes.class_num'))

# Teachers
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

# Courses
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), unique=True, nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.id'))
    teachers = db.relationship('Teachers', backref='courses')

# Classes
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_num = db.Column(db.String(50), nullable=False, unique=True)
    schedules = db.relationship('Schedules', backref='classes')