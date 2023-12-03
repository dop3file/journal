import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class StudentGroup(models.Model):
    title = models.CharField(max_length=256, blank=True, verbose_name="Название учебной группы", unique=True)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=256, blank=True, verbose_name="Фамилия")
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    birth_year = models.IntegerField()
    join_year = models.IntegerField()

    def __str__(self):
        return "User(<{}>)".format(self.username)