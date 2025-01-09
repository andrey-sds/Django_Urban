from django.urls import path
from .views import index, ClassPage


app_name = 'task2'

urlpatterns = [
    path('', index),
    path('class/', ClassPage.as_view())
]
