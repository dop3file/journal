import json
import logging
import datetime

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .services import UserService
from .controllers import AnthropometricTableControllers, FunctionalTableControllers
from .models import Anthropometric, Functional


anthropometric_table_controllers = AnthropometricTableControllers(Anthropometric, ("user", "semester", "id"))
functional_table_controllers = FunctionalTableControllers(Functional, ("user", "semester", "id"))


class ProfileView(TemplateView, View):
    template_name = "profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        profile_user = UserService.get(kwargs["pk"])
        context = {
            "is_own": request.user.id == profile_user.id,
            "profile_user": profile_user,
            "course": profile_user.get_course(),
            "age": profile_user.get_age_caption(),
            "count": range(1, 9),
            "user": request.user,
            "title": f"{profile_user.last_name} {profile_user.first_name}",
            "gender": "Мужской" if profile_user.gender == "male" else "Женский"
        }
        antropometric_data = anthropometric_table_controllers.get_table(profile_user)
        context.update(antropometric_data)
        context.update(anthropometric_table_controllers.calculate_indexes_physical_development(antropometric_data, profile_user.get_age()))
        functional_data = functional_table_controllers.get_table(profile_user)
        context.update(functional_data)
        return self.render_to_response(context)

    def post(self, request: HttpRequest, *args, **kwargs):
        anthropometric_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class FunctionalTableView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        functional_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class EditProfileView(TemplateView, View):
    template_name = "edit_profile.html"
    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({})



