from django.shortcuts import render
from django.http import HttpResponse

from .models import *

import datetime
import pytz

def index(request):
    elems = AlbumElem.objects.all().order_by('-id')
    return render(request, 'main/index.html', {'album_elem_list': elems})


def about(request):
    return render(request, 'main/about.html')


def archive(request, year):
    return HttpResponse(f"<h1>{year}</h1>")
