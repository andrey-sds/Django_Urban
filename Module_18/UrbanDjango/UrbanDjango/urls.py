"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task4', include('task4.urls', namespace='task4')),
    path('task3', include('task3.urls', namespace='task3')),
    path('lesson2/', include('task2.urls', namespace='task2')),
    path('django_sign_up/', include('task5.urls', namespace='task5')),
    path('', include('task5.urls', namespace='task5')),
]
