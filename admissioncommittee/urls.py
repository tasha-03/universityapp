from admissioncommittee import views
from django.urls import path


urlpatterns = [
    path('create-course/', views.create_course, name="create-course"),
    path('courses/', views.courses, name="courses"),
    path('edit-course/<int:id>/', views.edit_course),
    path('create-request/', views.create_request, name="create-request"),
    path('edit-request/<int:id>/', views.edit_request),
    path('', views.requests, name="admission-committee")
]
