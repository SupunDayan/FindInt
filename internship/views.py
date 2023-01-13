from django.shortcuts import render
from django.http import JsonResponse
from . models import Gig,Skill, ProLang, Internship
from . serializers import InternshipSerializer, SkillSerializer, ProLangSerializer, GigSerializer
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
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
