from django.contrib import admin

from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_of_creation', 'photo')
    list_display_links = ('title',)
    search_fields = ('id', 'title')
    list_filter = ('time_of_creation',)


admin.site.register(AlbumElem, MainAdmin)
