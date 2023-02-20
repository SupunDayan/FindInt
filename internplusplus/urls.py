
from django.contrib import admin
from student_det import views
from internship import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [                        
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('user/',include('user.urls')),
    path('internships/' ,include('internship.urls')),
    path('student-det/' ,include('student_det.urls')),
    path('company/' ,include('company.urls')), 
]
