from django.urls import path
from student_app import views


# URLConf
urlpatterns = [
    path('file/', views.file_upload),
    path('name/', views.change_name),
    
]