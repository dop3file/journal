import json

from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import EditProfileForm
from users.services import UserService
from .controllers import AnthropometricTableControllers, FunctionalTableControllers, ProfileControllers, \
    PhysicalStandardsControllers
from .models import Anthropometric, Functional, PhysicalStandards


anthropometric_table_controllers = AnthropometricTableControllers(Anthropometric, ("user", "semester", "id"))
functional_table_controllers = FunctionalTableControllers(Functional, ("user", "semester", "id"))
physicals_standards = PhysicalStandardsControllers(PhysicalStandards, ("user", "semester", "id"))
profile_controllers = ProfileControllers(
    anthropometric_table_controllers,
    functional_table_controllers,
    physicals_standards
)


class ProfileView(TemplateView, View):
    template_name = "profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        profile_user = UserService.get(kwargs["pk"])
        context = profile_controllers.get_profile_context(profile_user, request)
        return self.render_to_response(context)

    def post(self, request: HttpRequest, *args, **kwargs):
        anthropometric_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class FunctionalTableView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        functional_table_controllers.update_table(json.loads(request.body), request.user)
        return redirect("profile", pk=request.user.id)


class PhysicalStandartsTable(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        physicals_standards.update_table(json.loads(request.body), request.user)
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
            UserService.edit_group(request.user.id, group_id)
        return redirect("profile", pk=request.user.id)



