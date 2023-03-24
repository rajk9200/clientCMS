from flask_restful import Resource
from flask import Flask, request, jsonify,Response,abort
from cms.models import Student,Groups
from cms import db
from cms.serializer import student_people_schema, student_person_schema

class StudentView(Resource):
    def get(self):
        context={}
        Student_list = Student.query.all()
        if Student_list:
            result = student_people_schema.dump(Student_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404,"No Record Found.")
        return jsonify(context)
    def post(self):
        context={}
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        group_id = request.json.get('group_id')
        group = Groups.query.get(group_id)
        sub = Student(first_name=first_name,last_name=last_name,group_id=group_id)
        db.session.add(sub)
        db.session.commit()
        context['message'] = f"{first_name} student added successfully."
        return jsonify(context)

class StudentById(Resource):
    def get(self,id=None):
        context={}
        s=Student.query.filter_by(student_id=id)
        result = student_people_schema.dump(s)
        print(result)
        if not result.data:
            abort(404,"subject_id is not matched.")
        context['list']=result.data
        context['records']=len(result.data)
        return jsonify(context)
    def put(self,id=None):
        context={}
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        group_id = request.json.get('group_id')
        matched=Student.query.get(id)
        if not matched:
            abort(404,"Student id Invalid")
        group = Groups.query.get(group_id)
        if not group:
            abort(404, "Group id Invalid")

        Student.query.filter_by(student_id=id).update(dict(first_name=first_name,last_name=last_name,group_id=group_id))
        db.session.commit()
        context['message'] = f"{first_name} subject Update successfully."

        return jsonify(context)
    def delete(self,id=None):
        context={}
        matched = Student.query.get(id)
        if not matched:
            abort(404, "Student id not match")
        try:
            s = Student.query.filter_by(student_id=id).first()
            db.session.delete(s)
            db.session.commit()
            context['message'] = f"{id} subject deleted successfully."
        except Exception as e:
            abort(404, e)
        return jsonify(context)




