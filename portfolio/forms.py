from django import forms
from .models import Portfolio, PortfolioFiltre


class FiltreForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    choix = (
        ('portfolio-1.jpg', 'img1'),
        ('portfolio-2.jpg', 'img2'),
        ('portfolio-3.jpg', 'img3'),
        ('portfolio-4.jpg', 'img4'),
        ('portfolio-5.jpg', 'img5'),
        ('portfolio-6.jpg', 'img6'),
    )
    img = forms.ChoiceField(choices=choix)
    
    class Meta:
        model = PortfolioFiltre
        fields = '__all__'
