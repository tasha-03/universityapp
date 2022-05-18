from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from admissioncommittee.models import Course
from .forms import UserForm
from .models import User


def info(request, id):
    return HttpResponse("<h1>Профиль пользователя {0}</h1>".format(id))


def marks(request, id):
    return HttpResponse("<h1>Оценки пользователя {0}</h1>".format(id))


def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect('../../all')
    except User.DoesNotExist:
        return HttpResponseNotFound


def edit(request, id):
    try:
        user = User.objects.get(id=id)
        if request.method == "POST":
            user.full_name = request.POST.get("full_name")
            course_id = request.POST.get("course")
            user.course = Course.objects.get(id=course_id)
            user.password = request.POST.get("password")
            user.save()
            return HttpResponseRedirect("../../all")
        else:
            return render(request, "userprofile/edit-user.html", context={"title": "Изменить профиль", "user": user, "courses": Course.objects.all()})
    except:
        return HttpResponseNotFound
        

def login(request):
    if request.method == "POST":
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            form_full_name = request.POST.get("full_name")
            form_course = Course.objects.get(id=request.POST.get("course"))
            form_password = request.POST.get("password")
            User.objects.create(full_name=form_full_name,
                                course=form_course, password=form_password)
            return render(request, "userprofile/show-created-profile.html", context={"title": "Профиль создан", "req": {"full_name": form_full_name, "course": form_course.code}})
        else:
            return render(request, "userprofile/login.html", context={"title": "Регистрация", "form": userForm})
    userForm = UserForm()
    return render(request, "userprofile/login.html", {"form": userForm})


def all(request):
    users = User.objects.all()
    return render(request, "userprofile/userlist.html", {"title": "Пользователи", "users": users})
