from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.alumnes, name ='alumnes'),
    path('', views.profes, name ='profes'),
    path('alumnos', views.alumnes, name='alumnes'),
    path('profesores', views.profes, name='profes'),
    path('alumnos/<str:pk>/', views.alumno, name='alumno'),
    path('alumnos/<str:pk>/', views.profesor, name='profesor'),
    path('user-form', views.user_form, name='user_form')
]