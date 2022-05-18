from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from userprofile.models import User
from userprofile.models import Anketa
from .forms import CourseForm
from .models import Course
from userprofile.forms import AnketaForm


def create_request(request):
    if request.method == "POST":
        form_user = User.objects.get(id=request.POST.get("user"))
        print(form_user.id)
        form_address = request.POST.get("address")
        form_birthday = request.POST.get("birthday")
        Anketa.objects.create(user=form_user, address=form_address, birthday=form_birthday)
        return render(request, "show-admission-request.html", context={"title": "Подача заявки на прием", "req": {"user": form_user, "address": form_address, "birthday": form_birthday}})
    else:
        anketaForm = AnketaForm()
        return render(request, "send-admission-request.html", context={"title": "Подача заявки на прием", "form": anketaForm})


def edit_request(request, id):
    try:
        anketa = Anketa.objects.get(id=id)
        if request.method == "POST":
            anketa.address = request.POST.get("address")
            anketa.birthday = request.POST.get("birthday")
            anketa.save()
            return HttpResponseRedirect("../../")
        else:
            return render(request, "edit-admission-request.html", context={"title": "Изменить курс", "anketa": anketa})
    except Course.DoesNotExist:
        return HttpResponseNotFound

#delete request ; delete course

def requests(request):
    anketas = Anketa.objects.all()
    return render(request, "admission-committee.html", context={"title": "Приемная комиссия 2022", "anketas": anketas})


def courses(request):
    courses = Course.objects.all()
    for course in courses:
        if course.cathedra == "1":
            course.cathedra = "Gryffindor"
        if course.cathedra == "2":
            course.cathedra = "Hufflepuff"
        if course.cathedra == "3":
            course.cathedra = "Ravenclaw"
        if course.cathedra == "4":
            course.cathedra = "Slytherin"
    return render(request, "courses.html", context={"title": "Курсы", "courses": courses})

# COURSEFORM


def create_course(request):
    if request.method == "POST":
        form_code = request.POST.get("code")
        form_cathedra = request.POST.get("cathedra")
        Course.objects.create(code=form_code, cathedra=form_cathedra)
        return render(request, "show-created-course.html", context={"title": "Курс создан", "req": {"code": form_code, "cathedra": form_cathedra}})
    else:
        courseForm = CourseForm()
        return render(request, "create-course.html", context={"title": "Подача заявки на прием", "form": courseForm})


def edit_course(request, id):
    try:
        course = Course.objects.get(id=id)
        if request.method == "POST":
            course.code = request.POST.get("code")
            course.cathedra = request.POST.get("cathedra")
            course.save()
            return HttpResponseRedirect("../../courses")
        else:
            return render(request, "edit-course.html", context={"title": "Изменить курс", "course": course})
    except Course.DoesNotExist:
        return HttpResponseNotFound
