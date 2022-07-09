from django.db import models


class AlbumElem(models.Model): # реализация непосредственно с SQLite
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    content = models.TextField(blank=True)
    time_of_creation = models.DateTimeField(auto_now_add=True)


