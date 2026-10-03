from django import forms
from .models import Lead, Manager


class CreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['user', 'number']


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['user', 'number', 'lead']
