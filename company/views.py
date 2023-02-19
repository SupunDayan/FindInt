from django.shortcuts import render
<<<<<<< HEAD
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

@api_view(['GET','PUT','DELETE'])
def company_id(request,id):
    try:
        company_obj = company.objects.get(id = id)
    
    except company_obj.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        serializer = companySerializer(company_obj)
        return Response(serializer.data)

    if(request.method == 'PUT'):
        serializer = companySerializer(company_obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    if(request.method == 'DELETE'):
        company_obj.delete()
=======

# Create your views here.
>>>>>>> internship
