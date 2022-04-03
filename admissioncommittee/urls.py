from admissioncommittee import views
from django.urls import path


urlpatterns = [
    path('<int:id>/', views.send),
    path('', views.info, name="admission-committee")
]