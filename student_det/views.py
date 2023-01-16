from django.shortcuts import render
from django.http import JsonResponse
from . models import StudentDet, Skill, ProLang
from . serializers import StudentDetSerializer,SkillSerializer,ProLangSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def student_det_list(request):
    studentDets = StudentDet.objects.all()
    serializer = StudentDetSerializer(studentDets, many = True)
    return Response(serializer.data)  

@api_view(['GET'])
def skill_list(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pro_lang_list(request):
    pro_langs = ProLang.objects.all()
    serializer = ProLangSerializer(pro_langs,many=True)
    return Response(serializer.data)


