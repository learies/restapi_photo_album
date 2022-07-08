from django.contrib import admin

from albums.models import Album, Photo

EMPTY_VALUE = '-пусто-'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Отобразить альбомы в админке."""
    list_display = (
        'pk', 'name', 'author', 'created'
    )
    search_fields = ('created',)
    empty_value_display = EMPTY_VALUE


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Отобразить фотографии в админке."""
    list_display = (
        'pk', 'album', 'name', 'image', 'created'
    )
    list_filter = ('album',)
    search_fields = ('name',)
    empty_value_display = EMPTY_VALUE
