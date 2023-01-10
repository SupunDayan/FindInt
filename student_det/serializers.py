from rest_framework import serializers
from student_det.models import StudentDet

class StudentDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDet
        fields = ['id','stu_name','degree','university','pro_email','linkedin','github']

