from django.shortcuts import render

# Create your views here.


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
    return render(request, 'fourth_task/main.html', context)


def shop(request):
    title = 'Игры'
    main_page = '/'
    shop = '/shop'
    recycle = '/recycle'

    context = {
        'title': title,
        'main_page': main_page,
        'shop': shop,
        'recycle': recycle,
        'games': ["Atomic Heart", "Cyberpunk 2077", "Half life 3"],

    }
    return render(request, 'fourth_task/shop.html', context)


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
    return render(request, 'fourth_task/recycle.html', context)