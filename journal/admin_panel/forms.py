from django import forms

from admin_panel.controllers import get_users_choices
from users.models import StudentGroup


class AdminForm(forms.Form):
    group = forms.ChoiceField(
        label="Студент",
        choices=get_users_choices,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Студент'}),
        required=True
    )


class StatisticsForm(forms.Form):
    group1 = forms.ModelChoiceField(
        label="Группа",
        queryset=StudentGroup.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Студент'}),
        empty_label=None
    )

