from django.urls import path
from .views import sign_up_by_django, sign_up_by_html


app_name = 'task5'

urlpatterns = [
    path('', sign_up_by_html),
    path('', sign_up_by_django),

]
