from cms import db, ma

from cms import models

class SubjectSerializer(ma.ModelSchema):
    class Meta:
        model = models.Subjects
        load_instance = True
        sqla_session = db.session


person_schema = models.Subjects()
people_schema = SubjectSerializer(many=True)


class StudentSerializer(ma.ModelSchema):
    class Meta:
        model = models.Student
        load_instance = True
        sqla_session = db.session


student_person_schema = models.Student()
student_people_schema = StudentSerializer(many=True)




class GroupSerializer(ma.ModelSchema):
    class Meta:
        model = models.Groups
        load_instance = True
        sqla_session = db.session


group_person_schema = models.Groups()
group_people_schema = GroupSerializer(many=True)




class MarkSerializer(ma.ModelSchema):
    class Meta:
        model = models.Mark
        load_instance = True
        sqla_session = db.session


mark_person_schema = models.Mark()
mark_people_schema = MarkSerializer(many=True)