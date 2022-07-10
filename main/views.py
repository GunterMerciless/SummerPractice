from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse

from .models import *


def index(request):
    elems = AlbumElem.objects.all().order_by('-id')
    return render(request, 'main/index.html', {'album_elem_list': elems, 'title': 'Главная'})


def about(request):
    return render(request, 'main/about.html', {'title': 'Справка'})


def show_album_elem(request, album_elem_id):
    elem = get_object_or_404(AlbumElem, pk=album_elem_id)
    return render(request, 'main/albumelem.html', {'album_elem': elem})


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('login')
    else:
        print('Tried to register: May be method is not POST?')
        form = UserAddForm()
    return render(request, 'main/registration.html', {'title': 'Регистрация', 'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, 'main/login.html', {'title': 'Войти', 'form': form})
    else:
        print('Tried to login: May be method is not POST?')
        form = UserLoginForm()
        return render(request, 'main/login.html', {'title': 'Войти', 'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')
