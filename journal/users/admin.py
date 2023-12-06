from django.contrib import admin

from .models import CustomUser, StudentGroup


admin.site.register(CustomUser)
admin.site.register(StudentGroup)