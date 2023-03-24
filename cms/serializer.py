from cms import db, ma

from cms import models
from marshmallow import Schema, fields
class SubjectSerializer(ma.ModelSchema):
    class Meta:
        model = models.Subjects
        fields = ('subject_id', 'title')


person_schema = models.Subjects()
people_schema = SubjectSerializer(many=True)

class GroupSerializer(ma.ModelSchema):
    class Meta:
        model = models.Groups
        fields = ('group_id', 'name')


group_person_schema = models.Groups()
group_people_schema = GroupSerializer(many=True)

class StudentSerializer(ma.ModelSchema):
    groups = fields.Nested(GroupSerializer)
    class Meta:
        model = models.Student
        fields = ('student_id', 'first_name','last_name','groups')


student_person_schema = models.Student()
student_people_schema = StudentSerializer(many=True)


class TeacherSerializer(ma.ModelSchema):
    subject = fields.Nested(SubjectSerializer)
    groups = fields.Nested(GroupSerializer)
    class Meta:
        model = models.Teacher
        fields = ('teacher_id','subject','groups')



tacher_person_schema = models.Teacher()
tacher_people_schema = TeacherSerializer(many=True)




class MarkSerializer(ma.ModelSchema):
    student = fields.Nested(StudentSerializer)
    subject = fields.Nested(SubjectSerializer)
    class Meta:
        model = models.Mark
        fields = ('mark_id','student', 'mark','subject','date')



mark_person_schema = models.Mark()
mark_people_schema = MarkSerializer(many=True)