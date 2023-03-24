#
from datetime import datetime
from cms import db

class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

class Groups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    group_id=db.Column(db.Integer, db.ForeignKey('groups.group_id'),
        nullable=True)
    groups = db.relationship("Groups", backref='groups')



#
class Mark(db.Model):
    mark_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'),
                         nullable=True)

    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'),
                           nullable=True)
    date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    mark = db.Column(db.Integer)

    subject = db.relationship("Subjects", foreign_keys=[subject_id])
    student = db.relationship("Student", foreign_keys=[student_id])










