from django.contrib import admin

from albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Отобразить альбомы в админке."""
    list_display = (
        'pk', 'name', 'author', 'created'
    )
    search_fields = ('created',)
    empty_value_display = '-пусто-'
