from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from admin_panel.forms import AdminForm
from profiles.controllers import ProfileControllers, FunctionalTableControllers, AnthropometricTableControllers, \
    PhysicalStandardsControllers
from profiles.models import Functional, Anthropometric, PhysicalStandards
from users.services import UserService


anthropometric_table_controllers = AnthropometricTableControllers(Anthropometric, ("user", "semester", "id"))
functional_table_controllers = FunctionalTableControllers(Functional, ("user", "semester", "id"))
physicals_standards = PhysicalStandardsControllers(PhysicalStandards, ("user", "semester", "id"))


class AdminPanelView(TemplateView, View):
    template_name = "admin.html"
    profile_controllers = ProfileControllers(anthropometric_table_controllers, functional_table_controllers, physicals_standards)

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({
            "form": AdminForm
        })

    def post(self, request: HttpRequest, *args, **kwargs):
        print(request.POST)
        context = {
            "form": AdminForm,
        }
        profile_user = UserService.get(request.POST.get("group"))
        context.update(self.profile_controllers.get_profile_context(profile_user, request))
        return self.render_to_response(context)
