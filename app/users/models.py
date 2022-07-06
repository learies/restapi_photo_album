from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy as _

models.CharField.register_lookup(Length)


class User(AbstractUser):
    """Модель пользователя. Все поля обязательны для заполнения."""
    email: str = models.EmailField(
        verbose_name=_('Email'),
        max_length=254,
        unique=True,
    )
    username: str = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=True,
    )
    password: str = models.CharField(
        verbose_name=_('password'),
        max_length=150,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            models.CheckConstraint(
                check=models.Q(username__length__gte=3),
                name='\nслишком короткое имя пользователя\n',
            ),
        )

    def __str__(self):
        return f'{self.username}: {self.email}'
