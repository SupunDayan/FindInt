from django.shortcuts import render
from django.http import JsonResponse
from . models import Skill, ProLang, Internship
from . serializers import InternshipSerializer, SkillSerializer, ProLangSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def internship_list(request):
    if(request.method == 'GET'):
        internships = Internship.objects.all()
        serializer = InternshipSerializer(internships, many = True)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = InternshipSerializer(data = request.data)
        if serializer.is_valid():
            internship = serializer.save()
            create_skills(request,internship)
            create_ProLangs(request, internship)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

def create_skills(request,internship):
    skills = request.data["skills"].split(", ")
    for skill in skills :
        skill_serializer = SkillSerializer(data = {'skill':skill,'Internship':internship.id})
        if skill_serializer.is_valid():
            skill_serializer.save()
        
def create_ProLangs(request, internship):
    Pro_Langs = request.data["programming_languages"].split(", ")
    for ProLang in Pro_Langs :
        ProLang_serializer = ProLangSerializer(data = {'ProLang':ProLang,'Internship':internship.id})
        if ProLang_serializer.is_valid():
            ProLang_serializer.save()


@api_view(['GET','PUT','DELETE'])
def internship_update(request,id):
    try:
        internship = Internship.objects.get(id = id)
    
    except internship.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        serializer = InternshipSerializer(internship)
        return Response(serializer.data)

    if(request.method == 'PUT'):
        serializer = InternshipSerializer(internship, data = request.data)
        if serializer.is_valid():
            internship = serializer.save()
            delete_skills(internship)
            delete_ProLangs(internship)
            create_skills(request,internship)
            create_ProLangs(request, internship)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    if(request.method == 'DELETE'):
        internship.delete()

def delete_skills(internship):
    skills=  Skill.objects.filter(Internship=internship.id)
    skills.delete()

def delete_ProLangs(internship):
    ProLangs=  ProLang.objects.filter(Internship=internship.id)
    ProLangs.delete()


@api_view(['GET', 'POST'])
def intern_detail_by_title(request, *args, **kwargs) :
    
    try:
        params = kwargs
        internships = Internship.objects.filter(title=params['title'])
    except Internship.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    elif request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def intern_detail_by_category(request, *args, **kwargs) :
    
    try:
        params = kwargs
        internships = Internship.objects.filter(category=params['category'])
    except Internship.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    elif request.method == 'POST':
        pass










