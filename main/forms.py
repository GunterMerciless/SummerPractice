from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserAddForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Логин"}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Пароль"}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Логин"}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Пароль"}))
