from rest_framework import serializers
from student_det.models import StudentDet,Skill,ProLang

class StudentDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDet
        fields = ['id','stu_name','degree','university','pro_email','linkedin','github']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','student_det','skill']

class ProLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProLang
        fields = ['id','student_det','language']