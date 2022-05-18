from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from .forms import NewsForm
from .models import News


def create(request):
    if request.method == "POST":
        newsForm = NewsForm(request.POST)
        if newsForm.is_valid():
            title = request.POST.get("title")
            text = request.POST.get("text")
            rating = request.POST.get("rating")
            date = request.POST.get("date")
            News.objects.create(title=title, text=text, rating=rating, date=date)
            return render(request, "news/show-created-news.html", context={"title": "Новость создана", "req": {"title": title, "date": date, "text": text, "rating": rating}})
        else:
            return render(request, "news/create-news.html", context={"title": "Создание новости", "form": newsForm})
    newsForm = NewsForm()
    return render(request, "news/create-news.html", context={"title": "Создание новости", "form": newsForm})

def edit(request, id):
    try:
        news = News.objects.get(id=id)
        if request.method == "POST":
            news.title = request.POST.get("title")
            news.text = request.POST.get("text")
            news.rating = request.POST.get("rating")
            news.date = request.POST.get("date")
            news.save()
            return HttpResponseRedirect("../../")
        else:
            return render(request, "news/edit-news.html", context={"title": "Изменить новость", "news": news})
    except:
        return HttpResponseNotFound

def delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return HttpResponseRedirect('../../')
    except News.DoesNotExist:
        return HttpResponseNotFound

def show(request, id):
    news = News.objects.get(id=id)
    return render(request, "news/news-page.html", context={"news": news, "title": "{0} - Новости".format(news.title)})


def all(request):
    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 10)
    news = News.objects.all()
    return render(request, "news/news.html", context={"news": news, "title": "Новости"})
