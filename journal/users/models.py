import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = 'male', _('male')
    WOOMAN = 'wooman', _('wooman')


class StudentGroup(models.Model):
    title = models.CharField(max_length=256, blank=True, verbose_name="Название учебной группы", unique=True)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=256, blank=True, verbose_name="Фамилия")
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    birth_year = models.IntegerField(default=None, null=True)
    join_year = models.IntegerField(default=None, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=128, default="male")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_age_caption(self) -> str:
        age_token = lambda age_to: (
                (age_to in range(5, 20)) and 'лет' or
                (1 in (age_to, (diglast := age_to % 10))) and 'год' or
                ({age_to, diglast} & {2, 3, 4}) and 'года' or 'лет')
        age = datetime.datetime.now().year - self.birth_year
        return f"{age} {age_token(age)}"

    def get_age(self) -> int:
        age = datetime.datetime.now().year - self.birth_year
        return age

    def get_course(self) -> int:
        return datetime.datetime.now().year - self.join_year + 1

