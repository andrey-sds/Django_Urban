from django.urls import path
from .views import main, shop, recycle, sign_up_by_django


app_name = 'task1'

urlpatterns = [
    path('', main),
    path('shop/', shop),
    path('recycle/', recycle),
    path('sign/', sign_up_by_django),
]
