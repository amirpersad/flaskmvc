from App.database import db


class Course(db.Model):
    name = db.Column(db.String(100), primary_key=True)

    def __init__(self, name):
        self.name = name
