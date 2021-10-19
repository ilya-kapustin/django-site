from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    social = forms.CharField(label='Соц сеть', required=False)
    img = forms.FileField(help_text='Изображение профиля')
    address = forms.CharField(max_length=255, help_text='Адрес')
    brightday = forms.DateField()


class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    img = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'img')
