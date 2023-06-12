from django import forms
from .models import Skills, Skills_bar


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class Skills_barForm(forms.ModelForm):
    class Meta:
        model = Skills_bar
        fields = '__all__'
