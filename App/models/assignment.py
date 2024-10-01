from App.database import db
from App.models import Course
from App.models import Staff

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Integer, db.ForeignKey('course.name'),nullable=False)
    staff_id = db.Column(db.Integer,db.ForeignKey('staff.id'), nullable=False)

    course = db.relationship('Course', backref=db.backref('assignments', lazy=True))
    staff = db.relationship('Staff', backref=db.backref('assignments', lazy=True))


