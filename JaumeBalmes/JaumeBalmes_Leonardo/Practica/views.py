from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


# Create your views here.

alumnos = [
        {"id": "1","nombre":"Leo", "surname":"Chávez", "age":"20"},
        {"id": "2","nombre":"Luis", "surname":"Chávez", "age":"50"},
        {"id": "3","nombre":"Pepo", "surname":"Happy", "age":"12"},
        {"id": "4","nombre":"Roger", "surname":"Sobrino", "age":"12"},
        {"id": "5","nombre":"Javier", "surname":"Roca", "age":"12"},
        {"id": "6","nombre":"Jonathan", "surname":"Valle", "age":"12"},
    ]

profesores = [
        {"id": "1","nombre":"Roger", "curso":"a", "ufs":"1"},
        {"id": "2","nombre":"Oriol", "curso":"b", "ufs":"2"},
        {"id": "3","nombre":"Oriol", "curso":"c", "ufs":"3"},
    ]

def alumnes(request):

    context = {'als': alumnos}
    return render(request, 'alumnos.html',context)


def profes(request):
    context = {'pfs': profesores}
    return render(request, 'profesores.html', context)

def alumno(request, pk):
    alumno_Obj = None
    for i in alumnos:
        if i['id'] == pk:
            alumno_Obj = i
    return render(request, 'alumno.html', {'al':alumno_Obj})

def profesor(request, pk):
    profesor_Obj = None
    for i in profesores:
        if i['id'] == pk:
            profesor_Obj = i
    return render(request, 'profesor.html', {'pf':profesor_Obj})

# def index(request):
#     profesor = {"name":"Leo", "surname":"Chávez", "age":"20"}
#     return render(request, 'index.html', {'nombre':profesor["name"], 'apellido':profesor["surname"], 'años':profesor["age"]} )
