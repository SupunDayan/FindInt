from django.shortcuts import render
from django.http import JsonResponse
from . models import StudentDet, Skills, ProLang
from . serializers import StudentDetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def student_det_list(request):
    studentDets = StudentDet.objects.all()
    serializer = StudentDetSerializer(studentDets, many = True)
    return Response( serializer.data) 