from flask_restful import Resource
from flask import Flask, request, jsonify,Response,abort
from cms.models import Subjects,Groups,Mark,Student
from cms import db
from cms.serializer import mark_people_schema, mark_person_schema

class MarkView(Resource):
    def get(self):
        context={}
        mark_list = Mark.query.all()
        if mark_list:
            result = mark_people_schema.dump(mark_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404,"No Record Found.")
        return jsonify(context)
    def post(self):
        context={}
        student_id = request.json.get('student_id')
        subject_id = request.json.get('subject_id')
        mark = request.json.get('mark')
        matched = Subjects.query.get(subject_id)
        if not matched:
            abort(404, "Subject id is invalid")
        matched = Student.query.get(student_id)
        if not matched:
            abort(404, "Student id is invalid")
        sub = Mark(student_id=student_id, subject_id=subject_id, mark=mark)
        db.session.add(sub)
        db.session.commit()
        context['message'] = f"1 mark added successfully."
        return jsonify(context)

class MarkById(Resource):
    def get(self,id=None):
        context={}
        mark_list=Mark.query.filter_by(mark_id=id)
        result = mark_people_schema.dump(mark_list)
        print(result)
        matched = Mark.query.get(id)
        if not matched:
            abort(404, "Mark id Invalid.")
        context['list']=result.data
        context['records']=len(result.data)
        return jsonify(context)
    def put(self,id=None):
        context={}
        matched = Mark.query.get(id)
        if not matched:
            abort(404, "Mark id Invalid.")
        student_id = request.json.get('student_id')
        subject_id = request.json.get('subject_id')
        mark = request.json.get('mark')

        matched = Subjects.query.get(subject_id)
        if not matched:
            abort(404, "Subject id is invalid")
        matched = Student.query.get(student_id)
        if not matched:
            abort(404, "Student id is invalid")

        Mark.query.filter_by(mark_id=id).update(dict(student_id=student_id, subject_id=subject_id, mark=mark))
        db.session.commit()
        context['message'] = f"mark Update successfully."

        return jsonify(context)
    def delete(self,id=None):
        context={}
        matched = Mark.query.get(id)
        if not matched:
            abort(404, "Mark id Invalid.")
        try:
            s = Mark.query.filter_by(mark_id=id).first()
            db.session.delete(s)
            db.session.commit()
            context['message'] = f"Mark id {id}  deleted successfully."
        except Exception as e:
            abort(404, e)
        return jsonify(context)




