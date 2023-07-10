# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Логин',
        max_length=settings.MAXIMUM_LEN,
        unique=True,
    )
    email = models.EmailField(
        'Email',
        max_length=settings.MAXIMUM_LEN,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=settings.MAXIMUM_LEN,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=settings.MAXIMUM_LEN,
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}, {self.email}'
