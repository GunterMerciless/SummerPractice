from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('favorites', favorites, name='favorites'),
    path('about', about, name='about'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('registration', registration, name='reg'),
    path('albumelem/<int:album_elem_id>/', show_album_elem, name='albumelem')
]

