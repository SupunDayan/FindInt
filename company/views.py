from django.shortcuts import render
from django.http import JsonResponse
from . models import company
from . serializers import companySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])

def company_list(request):
    if(request.method == 'GET'):
        companies = company.objects.all()
        serializer = companySerializer(companies, many = True)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = companySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
