from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


# Create your views here.
def index(request):


    profesor = {"name":"Leo", "surname":"Chávez", "age":"20"}
    return render(request, 'index.html', {'nombre':profesor["name"], 'apellido':profesor["surname"], 'años':profesor["age"]} )