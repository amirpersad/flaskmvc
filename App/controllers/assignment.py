from App.database import db
from App.models import Staff
from App.models import Course
from App.models import Assignment

def assign_staff():
    course_name = input("Enter Course Name: ")
    staff_id = input("Enter Staff ID: ")
    assignment = Assignment(course_name=course_name, staff_id=staff_id)
    db.session.add(assignment)
    db.session.commit()
    print("Staff Assigned!")

def view_course_staff():
    name = input("Enter course Name: ")
    course = Course.query.get(name)
    if not course:
        print("Course not found.")
        return
    print(f'Staff for Course {course.name}:')
    for assignment in course.assignments:
        staff = Staff.query.get(assignment.staff_id)
        print(f'{staff.name} - {staff.role}')
    