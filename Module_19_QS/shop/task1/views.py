from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.
info = {}


def main(request):
    title = 'Главная страница'
    main_page = '/'
    shop = '/shop'
    recycle = '/recycle'

    context = {
        'title': title,
        'main_page': main_page,
        'shop': shop,
        'recycle': recycle,

    }
    return render(request, 'main.html', context)


def shop(request):
    title = 'Игры'
    main_page = '/'
    shop = '/shop'
    recycle = '/recycle'
    games = Game.objects.all()
    context = {
        'title': title,
        'main_page': main_page,
        'shop': shop,
        'recycle': recycle,
        'games': games,

    }
    return render(request, 'shop.html', context)


def recycle(request):
    title = 'Корзина'
    main_page = '/'
    shop = '/shop'
    recycle = '/recycle'

    context = {
        'title': title,
        'main_page': main_page,
        'shop': shop,
        'recycle': recycle,

    }
    return render(request, 'recycle.html', context)


def sign_up_by_django(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = int(form.cleaned_data['age'])
            if Buyer.objects.filter(name__exact=username):
                info['error'] = 'Пользователь уже существует!'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['success'] = f"Приветствуем, {username}!"
            # Проверяем, совпадают ли пароли
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'

            # Проверяем возраст
            # age = form.cleaned_data['age']
            # if int(age) < 18:
            #     info['error'] = 'Вы должны быть старше 18!'

    else:
        form = UserRegister()

    context = {
        'form': form,
        'info': info

    }

    return render(request, 'registration_page.html', context)
