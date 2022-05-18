from news import views
from django.urls import path


urlpatterns = [
    path('create', views.create, name="create_news"),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('<int:id>/', views.show, name="single_news"),
    path('', views.all, name="news")
]