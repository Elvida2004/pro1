from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True,verbose_name="Логин")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество")
    phone = models.CharField(max_length=17, unique=True,verbose_name="Телефон")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"