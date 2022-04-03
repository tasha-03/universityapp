from userprofile import views
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<int:id>/', include([
        path('info/', views.info),
        path('marks/', views.marks)
    ])),
    path('<int:id>/', RedirectView.as_view(url='info/', permanent=False)),
    
    path('', views.login, name="profile")
]