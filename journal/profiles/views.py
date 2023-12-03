import logging
import datetime

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .services import UserService
from .controllers import get_anthropometric


class ProfileView(TemplateView, View):
    template_name = "profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        user = UserService.get(kwargs["username"])
        now = datetime.datetime.now()
        course = now.year - user.join_year + 1
        age = now.year - user.birth_year
        context = {
            "is_own": request.user.id == user.id,
            "user": user,
            "course": course,
            "age": age
        }
        context.update(get_anthropometric(user))
        return self.render_to_response(context)



