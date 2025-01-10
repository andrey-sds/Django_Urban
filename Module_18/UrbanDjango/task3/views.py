from django.shortcuts import render

# Create your views here.


def main(request):
    title = 'Добро пожаловать в магазин'
    main_page = '#'
    shop = '/shop'
    recycle = '/recycle'
    back_page = '/'
    context = {
        'title': title,
        'main_page': main_page,
        'shop': shop,
        'recycle': recycle,
        'back_page': back_page
    }
    return render(request, 'third_task/main.html', context)


def shop(request):
    title = 'Игры'

    back_page = '/'
    context = {
        'title': title,
        'back_page': back_page
    }
    return render(request, 'third_task/shop.html', context)


def recycle(request):
    title = 'Корзина'
    back_page = '/'
    context = {
        'title': title,
        'back_page': back_page
    }
    return render(request, 'third_task/recycle.html', context)