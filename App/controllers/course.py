from App.database import db
from App.models import Course

def create_course():
    name = input("Enter course name: ")
    course = Course(name=name)
    db.session.add(course)
    db.session.commit()
    print("Course created!")
