from django import forms

from admin_panel.controllers import get_group_choices


class AdminForm(forms.Form):
    group = forms.ChoiceField(
        label="Учебная группа",
        choices=get_group_choices,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Учебная группа'}),
        required=True
    )
