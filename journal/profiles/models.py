from django.db import models
from users.models import CustomUser


class Anthropometric(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    vital_capacity = models.FloatField(blank=True, null=True)
    strength = models.FloatField(blank=True, null=True)
    right_hand_strength = models.FloatField(blank=True, null=True)
    left_hand_strength = models.FloatField(blank=True, null=True)
    chs = models.FloatField(blank=True, null=True)
    ads = models.FloatField(blank=True, null=True)
    add = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.semester} семестр {self.user}"


class Functional(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester = models.IntegerField(blank=True, null=True)
    genchi = models.FloatField(blank=True, null=True)
    shtange = models.FloatField(blank=True, null=True)
    functional_ccc = models.FloatField(blank=True, null=True)
    orthostatic = models.FloatField(blank=True, null=True)

