from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput, TextInput

from .models import CustomUser, StudentGroup
import datetime


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Никнейм',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'})
    )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )

    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'Email'})
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'})
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'})
    )

    join_year = forms.IntegerField(
        label='Год поступления',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Год поступления(пример 2021)'}),
        max_value=datetime.date.today().year
    )

    group = forms.ModelChoiceField(
        label="Учебная группа",
        queryset=StudentGroup.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Учебная группа'}),
        required=True
    )

    birth_year = forms.IntegerField(
        label="Год рождения",
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Год рождения'})
    )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        user.first_name = first_name
        user.last_name = last_name
        user.group = self.cleaned_data["group"]
        user.email = self.cleaned_data["email"]
        user.join_year = int(self.cleaned_data["join_year"])
        user.birth_year = int(self.cleaned_data["birth_year"])
        if commit:
            user.save()
        return user

    class Meta:
        fields = ("first_name", "last_name", "username", "password1", "password2", "email")
        model = CustomUser


class LoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        widgets = {
            "username": TextInput({'class': 'form-control', 'placeholder': 'Никнейм'}),
            "password": PasswordInput({'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'})
        }


