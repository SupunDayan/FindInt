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








