from schedule import views
from django.urls import path


urlpatterns = [
    path('<int:id>/', views.show, name="single_schedule"),
    path('', views.all, name="schedule")
]