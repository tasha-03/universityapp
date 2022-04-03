from django.http import HttpResponse
from django.shortcuts import render

def send(request, id):
    return HttpResponse("<h1>Страница подачи заявки на прием {0}</h1>".format(id))

def info(request):
    return render(request, "admission-committee.html", context={"title": "Приемная комиссия 2022"})
