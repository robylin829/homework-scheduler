from enum import unique

from sqlalchemy import null
from app import db

# Schedule - course - teacher

# Each class schedule
class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # When is the course
    day = db.Column(db.String(10), nullable=False)
    courses = db.relationship("Courses", backref="schedules")

# Teachers
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    

# Courses
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), unique=True, nullable=False)
