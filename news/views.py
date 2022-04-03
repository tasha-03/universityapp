from django.http import HttpResponse
from django.shortcuts import render

news = [
    {"id": 0, "title": "1234567890", "text": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diem nonummy nibh euismod tincidunt ut lacreet dolore magna aliguam erat volutpat. Ut wisis enim ad minim veniam, quis nostrud exerci tution ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat."},
    {"id": 1, "title": "0987654321", "text": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diem nonummy nibh euismod tincidunt ut lacreet dolore magna aliguam erat volutpat. Ut wisis enim ad minim veniam, quis nostrud exerci tution ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat."},
    {"id": 2, "title": "qwertyuiop", "text": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diem nonummy nibh euismod tincidunt ut lacreet dolore magna aliguam erat volutpat. Ut wisis enim ad minim veniam, quis nostrud exerci tution ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat."}
]

def show(request, id):
    single_news = next((x for x in news if x["id"] == id), None)
    return render(request, "news-page.html", context={"news": single_news, "title": "{0} - Новости".format(single_news["title"])})

def all(request):
    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 10)
    return render(request, "news.html", context={"news": news, "title": "Новости"})
