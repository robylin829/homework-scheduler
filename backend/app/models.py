from app import db

class Schedule(db.Model):
    class_number = db.Column(db.Integer, primary_key=True)
    

class Courses(db.Model):
    pass