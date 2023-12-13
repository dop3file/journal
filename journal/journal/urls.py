"""
URL configuration for journal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users.views import MainView, RegisterView, LoginView, logout_endpoint
from profiles.views import ProfileView, FunctionalTableView, EditProfileView, PhysicalStandartsTable
from admin_panel.views import AdminPanelView, StatisticsView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', MainView.as_view(), name="main"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_endpoint, name='logout'),
    path('panel/', AdminPanelView.as_view(), name='panel'),
    path('functional_table/', FunctionalTableView.as_view(), name='functional'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('physicals_table/', PhysicalStandartsTable.as_view(), name='physicals'),
    path('statistics/', StatisticsView.as_view(), name='statistics')
]
