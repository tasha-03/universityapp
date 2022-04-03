"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from handlers import views as handlers
from django.views.generic.base import RedirectView

handler304 = handlers.m304
handler400 = handlers.m400
handler403 = handlers.m403
handler404 = handlers.m404
handler405 = handlers.m405
handler410 = handlers.m410
handler500 = handlers.m500

urlpatterns = [
    path('profile/', include('userprofile.urls')),
    path('news/', include('news.urls')),
    path('schedule/', include('schedule.urls')),
    path('admission-committee/', include('admissioncommittee.urls'), ),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='news/', permanent=False))
]
