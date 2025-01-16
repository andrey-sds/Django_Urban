from django.urls import path
from .views import main, shop, recycle, sign_up_by_django, news_list, contacts


app_name = 'task1'

urlpatterns = [
       path('', main, name='main'),
       path('shop/', shop, name='shop'),
       path('recycle/', recycle, name='recycle'),
       path('sign/', sign_up_by_django, name='sign_up'),
       path('platform/news/', news_list, name='news_list'),
       path('platform/news/<int:page>/', news_list, name='news_list_paginated'),
       path('contacts/', contacts, name='contacts'),
]
