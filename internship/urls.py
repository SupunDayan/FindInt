from django.urls import path
from . import views

urlpatterns = [
    path('', views.internship_list),
    path('<int:id>',views.internship_update),
    path('<str:title>' , views.intern_detail_by_title),
    path('<str:category>' , views.intern_detail_by_category)
]