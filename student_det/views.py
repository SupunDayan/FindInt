from django.shortcuts import render
from django.http import JsonResponse
from . models import StudentDet, Skill, ProLang
from . serializers import StudentDetSerializer,SkillSerializer,ProLangSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])

def student_det_list(request):
    if(request.method == 'GET'):
        studentDets = StudentDet.objects.all()
        serializer = StudentDetSerializer(studentDets, many = True)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = StudentDetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def skill_list(request):
    if(request.method == 'GET'):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills,many=True)
        return Response(serializer.data)

    if(request.method == 'POST'):
        serializer = SkillSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def pro_lang_list(request):
    if(request.method == 'GET'):
        pro_langs = ProLang.objects.all()
        serializer = ProLangSerializer(pro_langs,many=True)
        return Response(serializer.data)

    if(request.method == 'POST'):
        serializer = ProLangSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

def returnSkill(id):
    studentDets = StudentDet.objects.all()
    skills = Skill.objects.all()
    stu_skills = list()
    for skill in skills:
        if skill.student_det.pk == studentDets[id].pk:
            stu_skills.append(skill.skill)
    print(stu_skills)
 