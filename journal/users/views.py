from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import RegisterForm, LoginForm
from .controllers import generate_anthropometric


class MainView(TemplateView, View):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response({
            "user": request.user,
            "title": "Journal"
        })


class RegisterView(TemplateView, View):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return self.render_to_response({
            "form": form,
            "title": "Регистрация"
        })

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            generate_anthropometric(user)
            login(request, user)
            return redirect("main")
        else:
            return self.render_to_response({"form": form})


class LoginView(TemplateView, View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return self.render_to_response({
            "form": form,
            "title": "Вход"
        })

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        if user is not None:
            if user.is_active:
                login(request, user)

        return redirect("main")


def _logout(request):
    logout(request)
    return redirect("main")
