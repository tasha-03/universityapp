from django.http import HttpResponse
from django.shortcuts import render


def info(request, id):
    return HttpResponse("<h1>Профиль пользователя {0}</h1>".format(id))

def marks(request, id):
    return HttpResponse("<h1>Оценки пользователя {0}</h1>".format(id))

def login(request):
    return render(request, "login.html")