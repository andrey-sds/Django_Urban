from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
# Create your views here.
users = ["Alex", "Sergey", "Max"]
info = {}


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверяем логин
        if username in users:
            info['error'] = 'Пользователь уже существует!'
            context = {
                'info': info
            }
            return render(request, 'fifth_task/registration_page.html', context)

        # Проверяем, совпадают ли пароли
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            context = {
                'info': info
            }
            return render(request, 'fifth_task/registration_page.html', context)

        # Проверяем возраст
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
            print(info)
            context = {
                'info': info
            }
            return render(request, 'fifth_task/registration_page.html', context)

        # Если все проверки пройдены
        else:
            users.append(username)
            info['success'] = f"Приветствуем, {username}!"
            context = {
                'info': info
            }
            return render(request, 'fifth_task/registration_page.html', context)

        # Если это не POST-запрос, просто отображаем форму
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if username in users:
                info['error'] = 'Пользователь уже существует!'
            else:
                users.append(username)
                info['success'] = f"Приветствуем, {username}!"
            # Проверяем, совпадают ли пароли
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'

            # Проверяем возраст
            age = form.cleaned_data['age']
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18!'

    else:
        form = UserRegister()

    context = {
        'form': form,
        'info': info
    }

    return render(request, 'fifth_task/registration_page.html', context)
