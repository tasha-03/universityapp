from django.http import HttpResponse
from django.shortcuts import render

schedules = [
    {"id": 0, "cathedra": "Гриффиндор", "filename": "griffindor.xlsx"},
    {"id": 1, "cathedra": "Райвенкло", "filename": "ravnclaw.xlsx"},
    {"id": 2, "cathedra": "Хаффлпафф", "filename": "hufflepuff.xlsx"},
    {"id": 3, "cathedra": "Слизерин", "filename": "slytherin.xlsx"},
]

def show(request, id):
    single_schedule = next((x for x in schedules if x["id"] == id), None)
    return render(request, "schedule-page.html", context={"schedule": single_schedule, "title": "{0} - Расписание".format(single_schedule["cathedra"])})

def all(request):
    return render(request, "schedule.html", context={"schedules": schedules, "title": "Расписание"})
