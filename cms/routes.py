from cms import app
from cms import api
from cms.views import subject,group,student,mark,teacher
from cms import db
from flask import send_from_directory
@app.route('/')
def index():
    return "welcome to my website"
# subjects crud
@app.route('/create_tables')
def ctables():
    db.create_all()
    return "Table Created Successfully.."


@app.route('/static/<path:path>')
def send_static(path):
    db.create_all()
    return send_from_directory('static',path)


# subject routes get,post ( getList,add new records)
# subject get by id, put, delete
api.add_resource(subject.SubjectView,'/subject')
api.add_resource(subject.SubjectById,'/subject/<id>')

# Group routes get,post ( getList,add new records)
# Group get by id, put, delete
api.add_resource(group.GroupView,'/group')
api.add_resource(group.GroupsById,'/group/<id>')



# Student routes get,post ( getList,add new records)
# Student get by id, put, delete
api.add_resource(student.StudentView,'/student')
api.add_resource(student.StudentById,'/student/<id>')



# Mark routes get,post ( getList,add new records)
# Makr get by id, put, delete
api.add_resource(mark.MarkView,'/mark')
api.add_resource(mark.MarkById,'/mark/<id>')



# Teacher routes get,post ( getList,add new records)
# Teacher get by id, put, delete
api.add_resource(teacher.TeacherView,'/teacher')
api.add_resource(teacher.TeacherViewById,'/teacher/<id>')



#http://127.0.0.1:5000/getmarks?student_id=4555
api.add_resource(mark.GetMarkByStudentID,'/getmarksbystudentId')
api.add_resource(teacher.GetStudentByTeacherID,'/getstudentbyteacherId')








