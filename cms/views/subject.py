from flask_restful import Resource
from flask import Flask, request, jsonify,Response,abort
from cms.models import Subjects
from cms import db
from cms.serializer import people_schema, person_schema

class SubjectView(Resource):
    def get(self):
        context={}
        subjects_list = Subjects.query.all()
        if subjects_list:
            result = people_schema.dump(subjects_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404,"No Record Found.")
        return jsonify(context)
    def post(self):
        context={}
        title = request.json.get('title')
        s=Subjects.query.filter_by(title=title)
        if s.all():
            abort(404, f"{title} already exists. try another.")
        sub = Subjects(title=title)
        db.session.add(sub)
        db.session.commit()
        context['message'] = f"{title} subject deleted successfully."
        return jsonify(context)

class SubjectById(Resource):
    def get(self,id=None):
        context={}
        s=Subjects.query.filter_by(subject_id=id)
        result = people_schema.dump(s)
        print(result)
        if not result.data:
            abort(404,"subject_id is not matched.")
        context['list']=result.data
        context['records']=len(result.data)
        return jsonify(context)
    def put(self,id=None):
        context={}
        matched=Subjects.query.get(id)
        if not matched:
            abort(404,"Student id not match")
        title = request.json.get('title')
        s = Subjects.query.filter_by(title=title)
        if s.all():
            abort(404, f"{title} already exists. try another.")
        Subjects.query.filter_by(subject_id=id).update(dict(title=title))
        db.session.commit()
        context['message'] = f"{title} subject Update successfully."

        return jsonify(context)
    def delete(self,id=None):
        context={}
        matched = Subjects.query.get(id)
        if not matched:
            abort(404, "Student id not match")
        try:
            s = Subjects.query.filter_by(subject_id=id).first()
            db.session.delete(s)
            db.session.commit()
            context['message'] = f"{id} subject deleted successfully."
        except Exception as e:
            abort(404, e)
        return jsonify(context)




