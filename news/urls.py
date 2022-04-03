from news import views
from django.urls import path


urlpatterns = [
    path('<int:id>/', views.show, name="single_news"),
    path('', views.all, name="news")
]