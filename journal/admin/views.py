from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class AdminPanelView(TemplateView, View):
    template_name = "admin.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request: HttpRequest, *args, **kwargs):
        ...
