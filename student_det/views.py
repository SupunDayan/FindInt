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

@api_view(['GET'])
def search_student(request, degree, uni):
    studentDets = StudentDet.objects.filter(degree = degree, university = uni)
    serializer = StudentDetSerializer(studentDets, many = True)
    return Response(serializer.data)

def returnSkill(id):
    studentDets = StudentDet.objects.all()
    skills = Skill.objects.all()
    stu_skills = list()
    for skill in skills:
        if skill.student_det.pk == studentDets[id].pk:
            stu_skills.append(skill.skill)
    print(stu_skills)

def returnProLang(id):
    studentDets = StudentDet.objects.all()
    pro_langs = ProLang.objects.all()
    stu_pro_langs = list()
    for pro_lang in pro_langs:
        if pro_lang.student_det.pk == studentDets[id].pk:
            stu_pro_langs.append(pro_lang.language)
    print(stu_pro_langs) 
    
@api_view(['GET','PUT','DELETE'])
def student_det_detail(request, id):
    try:
        studentDet = StudentDet.objects.get(pk=id)
        skill = iter(Skill.objects.filter(student_det = id))
        prolangs = iter(ProLang.objects.filter(student_det = id))
    except StudentDet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentDetSerializer(studentDet)      
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentDetSerializer(studentDet, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        for x in skill:
            x.delete()
        for x in prolangs:
            x.delete()
        studentDet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
