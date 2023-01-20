from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# from .models import Student
# from .serializers import StudentSerializer

def file_upload(request):
    return render(request, 'file_uploader.html')
     


def change_name(request):
    return render(request, 'change_name.html') 
