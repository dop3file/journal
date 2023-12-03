from django.db import models
from users.models import CustomUser


class Anthropometric(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    vital_capacity = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    right_hand_strength = models.IntegerField(blank=True, null=True)
    left_hand_strength = models.IntegerField(blank=True, null=True)
    chs = models.IntegerField(blank=True, null=True)
    ads = models.IntegerField(blank=True, null=True)
    add = models.IntegerField(blank=True, null=True)