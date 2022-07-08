from django.db import models

from users.models import User


class Album(models.Model):
    """Альбом с фотографиями."""
    name = models.CharField(
        verbose_name='Название альбома',
        max_length=200,
        help_text='Название альбома',
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        related_name='albums',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Фотографии в альбоме."""
    album = models.ForeignKey(
        to=Album,
        verbose_name='Фото',
        related_name='photo',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Название фото',
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='app/',
        blank=False,
        null=False,
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name
