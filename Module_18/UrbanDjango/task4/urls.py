from django.urls import path
from .views import main, shop, recycle


app_name = 'task4'

urlpatterns = [
    path('', main),
    path('shop/', shop),
    path('recycle/', recycle)
]
