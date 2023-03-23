from django.urls import path
from . import views

urlpatterns = [

    path('matadme', views.index, name = 'index')
]