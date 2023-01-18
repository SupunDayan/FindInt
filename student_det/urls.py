from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_det_list),
    path('skills', views.skill_list),
    path('pro_langs', views.pro_lang_list),
    path('search/<str:degree>,<str:uni>', views.search_student),
]
