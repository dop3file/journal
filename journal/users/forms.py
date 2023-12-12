from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput, TextInput

from .controllers import generate_physical_tables
from .models import CustomUser, StudentGroup
import datetime


class RegisterForm(UserCreationForm):
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

    gender = forms.ChoiceField(
        label="Пол",
        choices=[("male", "Мужской"), ("wooman", "Женский")],
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Пол'})
    )

    birth_year = forms.IntegerField(
        label="Год рождения",
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Год рождения'})
    )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        fields = CustomUser._meta.fields
        for field in fields:
            try:
                setattr(user, field.name, self.cleaned_data[field.name])
            except KeyError:
                ...
        user.username = user.email
        generate_physical_tables(user)
        if commit:
            user.save()
        return user

    class Meta:
        fields = ("first_name", "last_name", "password1", "password2", "email")
        model = CustomUser


class LoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password")
        widgets = {
            "email": TextInput({'class': 'form-control', 'placeholder': 'Email'}),
            "password": PasswordInput({'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'})
        }


