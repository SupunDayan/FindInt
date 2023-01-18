from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_det_list),
    path('skills', views.skill_list),
    path('pro_langs', views.pro_lang_list),
<<<<<<< HEAD
    path('search/<str:degree>,<str:uni>', views.search_student),
=======
    path('<int:id>',views.student_det_detail)
>>>>>>> 14d71b395843e774b5f7d740accc2e8e781e7e8f
]
