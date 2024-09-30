import os

from django.http import HttpRequest, FileResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from bokeh.plotting import figure
from bokeh.embed import components
import xlsxwriter

from admin_panel.controllers import GroupControllers
from admin_panel.forms import AdminForm, StatisticsForm
from profiles.controllers import ProfileControllers, FunctionalTableControllers, AnthropometricTableControllers, \
    PhysicalStandardsControllers, HealthControllers
from profiles.models import Functional, Anthropometric, PhysicalStandards, Health
from users.services import UserService


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
group_controllers = GroupControllers(profile_controllers)
user_service = UserService()


class AdminPanelView(TemplateView, View):
    template_name = "admin.html"
    title = "Админ панель"

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
        print(profile_user)
        context.update(profile_controllers.get_profile_context(profile_user, request))
        return self.render_to_response(context)


class StatisticsView(TemplateView, View):
    template_name = "statistics.html"
    title = "Статистика"

    def get(self, request: HttpRequest, *args, **kwargs):
        context = {
            "form": StatisticsForm
        }
        return self.render_to_response(context)

    def post(self, request: HttpRequest, *args, **kwargs):
        group1_id = int(request.POST.get("group1"))
        context = {
            "form": StatisticsForm,
            "group_id": group1_id
        }
        context.update(group_controllers.get_group_context(group1_id))
        return self.render_to_response(context)


def download_statistics(request, group_id: int):
    file_path = f'static/group_{group_id}.xlsx'
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')
    workbook.close()
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{group_id}_group.xlsx"'
    return response
