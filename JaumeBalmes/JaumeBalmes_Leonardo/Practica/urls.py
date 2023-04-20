from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.alumnes, name ='alumnes'),
    path('', views.profes, name ='profes'),
    path('alumnos', views.alumnes, name='alumnes'),
    path('profesores', views.profes, name='profes'),
    path('alumnos/<str:pk>/', views.alumno, name='alumno'),
    path('alumnos/<str:pk>/', views.profesor, name='profesor'),
    path('user-form', views.userForm, name='user_form'),
    path('usuario_registrados', views.users, name='index_one'),
    path('update_user/<str:pk>/', views.update_user, name='update_user'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user')
]