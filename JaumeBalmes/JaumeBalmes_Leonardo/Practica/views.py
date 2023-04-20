from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .models import Person
from .forms import PersonForm


# Create your views here.
# alumnos = [
#         {"id": "1","nombre":"Leo", "surname":"Chávez", "age":"20"},
#         {"id": "2","nombre":"Luis", "surname":"Castillo", "age":"50"},
#         {"id": "3","nombre":"Pepo", "surname":"Happy", "age":"12"},
#         {"id": "4","nombre":"Roger", "surname":"Sobrino", "age":"12"},
#         {"id": "5","nombre":"Javier", "surname":"Roca", "age":"12"},
#         {"id": "6","nombre":"Jonathan", "surname":"Valle", "age":"12"},
#     ]

profesores = [
        {"id": "1","nombre":"Roger", "curso":"a", "ufs":"1"},
        {"id": "2","nombre":"Oriol", "curso":"b", "ufs":"2"},
        {"id": "3","nombre":"Oriol", "curso":"c", "ufs":"3"},
    ]


def alumnes(request):
    alumnos = Person.objects.all()
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

# def user_form(request):
    # form = PersonForm(request.POST)

    # if request.method == 'POST':
    #     form = PersonForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index_one')


    # context = {'form':form}
    # return render(request, 'form.html', context)

def userForm(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index_one')
    context = {'form':form}
    return render(request, 'form.html', context)


def users(request):
    usuarios = Person.objects.all()
    context = {'users':usuarios}
    return  render(request, 'users.html', context)

def update_user(request, pk):
    person = Person.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance = person)
        if form.is_valid():
            form.save()
            return redirect('index_one')

    context = {'form':form}
    return render(request, 'form.html',context)

def delete_user(request, pk):
    person = Person.objects.get(id = pk)

    if request.method == 'POST':
        person.delete()
        return redirect('index_one')
    
    context = {'object':person}
    return render (request, 'delete_object.html', context)

# def index_one(request):
#     people = Person.objects.all()
#     context = {'people': people}
#     return render(request, 'index_one.html', context)

# def index(request):
#     profesor = {"name":"Leo", "surname":"Chávez", "age":"20"}
#     return render(request, 'index.html', {'nombre':profesor["name"], 'apellido':profesor["surname"], 'años':profesor["age"]} )
