from flask_restful import Resource
from flask import Flask, request, jsonify,abort,Response
from cms.models import Groups
from cms import db
from cms.serializer import group_people_schema, group_person_schema

class GroupView(Resource):
    def get(self):
        context={}
        Groups_list = Groups.query.all()
        if Groups_list:
            result = group_people_schema.dump(Groups_list)
            context['list'] = result.data
            context['records'] = len(result.data)
        else:
            abort(404,"No Record Found.")
        return jsonify(context)
    def post(self):
        context={}
        name = request.json.get('name')
        s=Groups.query.filter_by(name=name)
        if s.all():
            abort(404, f"{name} already exists. try another.")
        sub = Groups(name=name)
        db.session.add(sub)
        db.session.commit()
        context['message'] = f"{name} subject Added successfully."
        return Response(context=[],status=201)

class GroupsById(Resource):
    def get(self,id=None):
        context={}
        s=Groups.query.filter_by(group_id=id)
        result = group_people_schema.dump(s)
        print(result)
        if not result.data:
            abort(404,"group_id is not matched.")
        context['list']=result.data
        context['records']=len(result.data)
        return jsonify(context)
    def put(self,id=None):
        context={}
        matched=Groups.query.get(id)
        if not matched:
            abort(404,"Student id not match")
        name = request.json.get('name')
        s = Groups.query.filter_by(name=name)
        if s.all():
            abort(404, f"{name} already exists. try another.")
        Groups.query.filter_by(group_id=id).update(dict(name=name))
        db.session.commit()
        context['message'] = f"{name} group Update successfully."

        return jsonify(context)
    def delete(self,id=None):
        context={}
        matched = Groups.query.get(id)
        if not matched:
            abort(404, "Student id not match")
        try:
            s = Groups.query.filter_by(group_id=id).first()
            db.session.delete(s)
            db.session.commit()
            context['message'] = f"{id} subject deleted successfully."
        except Exception as e:
            abort(404, e)
        return jsonify(context)




