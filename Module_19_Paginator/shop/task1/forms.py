from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Имя пользователя', required=True)
    password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput)

    age = forms.IntegerField(min_value=1, max_value=150, label='Введите свой возраст')