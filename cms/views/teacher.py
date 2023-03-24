from flask_restful import Resource
from flask import Flask, request, jsonify,abort,Response
from cms.models import Groups,Teacher,Student,Subjects
from cms import db
from cms.serializer import tacher_people_schema, tacher_person_schema,student_people_schema

class TeacherView(Resource):
    def get(self):
        context={}
        teacher_list = Teacher.query.all()
        if teacher_list:
            result = tacher_people_schema.dump(teacher_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404,"No Record Found.")
        return jsonify(context)
    def post(self):
        context={}
        subject_id = request.json.get('subject_id')
        group_id = request.json.get('group_id')
        matched = Subjects.query.get(subject_id)
        if not matched:
            abort(404, "Subject id Invalid")
        group = Groups.query.get(group_id)
        if not group:
            abort(404, "Group id Invalid")
        s = Teacher.query.filter_by(subject_id=subject_id)
        if s.all():
            abort(404, f"Subject Id {subject_id} already exists. try another.")
        sub = Teacher(subject_id=subject_id,group_id=group_id)
        db.session.add(sub)
        db.session.commit()
        context['message'] = f" Teacher created successfully."
        return jsonify(context)

class TeacherViewById(Resource):
    def get(self,id=None):
        context={}
        s=Teacher.query.filter_by(teacher_id=id)
        result = tacher_people_schema.dump(s)
        if not result.data:
            abort(404,"teacher_id is invalid.")
        context['list']=result.data
        context['records']=len(result.data)
        return jsonify(context)

    def put(self,id=None):
        context={}
        subject_id = request.json.get('subject_id')
        group_id = request.json.get('group_id')
        matched = Subjects.query.get(subject_id)
        if not matched:
            abort(404, "Subject id Invalid")
        group = Groups.query.get(group_id)
        if not group:
            abort(404, "Group id Invalid")
        s = Teacher.query.filter_by(subject_id=subject_id)
        if s.all():
            abort(404, f"Subject Id {subject_id} already exists. try another.")
        Teacher.query.filter_by(teacher_id=id).update(dict(subject_id=subject_id, group_id=group_id))
        db.session.commit()
        context['message'] = f"Teacher updated successfully."

        return jsonify(context)
    def delete(self,id=None):
        context={}
        matched = Teacher.query.get(id)
        if not matched:
            abort(404, "Student id not match")
        try:
            s = Teacher.query.filter_by(teacher_id=id).first()
            db.session.delete(s)
            db.session.commit()
            context['message'] = f"{id} Teacher deleted successfully."
        except Exception as e:
            abort(404, e)
        return jsonify(context)



class GetStudentByTeacherID(Resource):
    def get(self):
        context = {}
        teacher_id = request.args.get('teacher_id')
        teacher_list = Teacher.query.filter(Teacher.teacher_id == teacher_id).first()
        new_subject_id =teacher_list.subject_id
        stu_list =Student.query.filter(Subjects.subject_id == new_subject_id).all()
        print(stu_list)
        if stu_list:
            result = student_people_schema.dump(stu_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404, "No Record Found.")
        return jsonify(context)



