from django.shortcuts import render
from django.http import JsonResponse
from . models import Company
from . serializers import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])

def company_list(request):
    if(request.method == 'GET'):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def company_id(request,id):
    try:
        company_obj = Company.objects.get(id = id)
    
    except company_obj.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        serializer = CompanySerializer(company_obj)
        return Response(serializer.data)

    if(request.method == 'PUT'):
        serializer = CompanySerializer(company_obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    if(request.method == 'DELETE'):
        company_obj.delete()
