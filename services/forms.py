from django import forms
from .models import Services


class ServicesForm(forms.ModelForm):
    choix = (
        ('bi-briefcase', 'bi-briefcase'),
        ('bi-card-checklist', 'bi-card-checklist'),
        ('bi-bar-chart', 'bi-bar-chart'),
        ('bi-binoculars', 'bi-binoculars'),
        ('bi-brightness-high', 'bi-brightness-high'),
        ('bi-calendar4-week', 'bi-calendar4-week'),
    )
    logo = forms.ChoiceField(choices=choix)
    class Meta:
        model = Services
        fields = '__all__'
