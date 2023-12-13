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
user_service = UserService()


class AdminPanelView(TemplateView, View):
    template_name = "admin.html"
    title = "Админ панель"
    profile_controllers = ProfileControllers(anthropometric_table_controllers, functional_table_controllers, physicals_standards)

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({
            "form": AdminForm,
            "title": self.title
        })

    def post(self, request: HttpRequest, *args, **kwargs):
        context = {
            "form": AdminForm,
        }
        profile_user = user_service.get(request.POST.get("group"))
        context.update(self.profile_controllers.get_profile_context(profile_user, request))
        return self.render_to_response(context)


class StatisticsView(TemplateView, View):
    template_name = "statistics.html"
    title = "Статистика"

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({
            "title": self.title
        })
