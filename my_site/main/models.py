from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class AlbumElem(models.Model):  # реализация непосредственно с SQLite
    photo = models.ImageField(upload_to='photos/')
    title = models.TextField(max_length=255, default='Название города')
    content = models.TextField(blank=True)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    bookmark = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('albumelem', kwargs={'album_elem_id': self.pk})

    class Meta:
        verbose_name = 'Статьи на сайте'
        verbose_name_plural = 'Статьи на сайте'
