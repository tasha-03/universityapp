from userprofile import views
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('all', views.all, name="all-users"),
    path('<int:id>/', include([
        path('info/', views.info),
        path('marks/', views.marks)
    ])),
    path('<int:id>/', RedirectView.as_view(url='info/', permanent=False)),
    path('', views.login, name="profile")
]