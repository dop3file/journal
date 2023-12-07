from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput, TextInput

from users.models import StudentGroup
from .models import CustomUser
import datetime


class EditProfileForm(ModelForm):
    group = forms.ModelChoiceField(
        label="Учебная группа",
        queryset=StudentGroup.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Учебная группа'}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ("group",)
        widgets = {
            "group": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Учебная группа'}),
        }


