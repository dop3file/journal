import json

from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .controllers import AnthropometricTableControllers, FunctionalTableControllers, PhysicalStandardsControllers, \
    ProfileControllers, HealthControllers
from .forms import EditProfileForm
from users.services import UserService
from .models import Anthropometric, Functional, PhysicalStandards, Health


anthropometric_table_controllers = AnthropometricTableControllers(Anthropometric, ("user", "semester", "id"))
functional_table_controllers = FunctionalTableControllers(Functional, ("user", "semester", "id"))
physicals_standards = PhysicalStandardsControllers(PhysicalStandards, ("user", "semester", "id"))
health_controllers = HealthControllers(Health, ("user", "lesson_number", "id"))
profile_controllers = ProfileControllers(
    anthropometric_table_controllers,
    functional_table_controllers,
    physicals_standards,
    health_controllers
)
user_service = UserService()


class ProfileView(TemplateView, View):
    template_name = "profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        profile_user = user_service.get(kwargs["pk"])
        context = profile_controllers.get_profile_context(profile_user, request)
        return self.render_to_response(context)

    def post(self, request: HttpRequest, *args, **kwargs):
        anthropometric_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class FunctionalTableView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        functional_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class PhysicalStandartsTableView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        physicals_standards.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class HealthTableView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        health_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class EditProfileView(TemplateView, View):
    template_name = "edit_profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        form = EditProfileForm()
        return self.render_to_response({
            "form": form
        })

    def post(self, request: HttpRequest, *args, **kwargs):
        group_id = request.POST.get("group")
        if group_id:
            user_service.edit_group(request.user.id, group_id)
        return redirect("profile", pk=request.user.id)



