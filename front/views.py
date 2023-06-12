from django.shortcuts import render
from about.models import About
from skills.models import Skills,Skills_bar
from services.models import Services
from testimonials.models import Testimonials
from contact.models import Contact
from portfolio.models import Portfolio, PortfolioFiltre

# Create your views here.
def homepage(request):
    abouts = About.objects.all()
    skills = Skills.objects.all()
    skills_bar = Skills_bar.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    portfolioFiltre = PortfolioFiltre.objects.all()
    return render(request, 'projet_2/front/home.html', {'abouts': abouts, 'skills': skills, 'skills_bar': skills_bar, 'services': services, 'testimonials': testimonials, 'contact': contact, 'portfolio': portfolio, 'portfolioFiltre': portfolioFiltre})


def home(request):
    abouts = About.objects.all()
    skills = Skills.objects.all()
    skills_bar = Skills_bar.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    portfolioFiltre = PortfolioFiltre.objects.all()
    return render(request, 'projet_2/front/home.html', {'abouts': abouts, 'skills': skills, 'skills_bar': skills_bar, 'services': services, 'testimonials': testimonials, 'contact': contact, 'portfolio': portfolio, 'portfolioFiltre': portfolioFiltre})

def backoffice(request):
    abouts = About.objects.all()
    skills = Skills.objects.all()
    skills_bar = Skills_bar.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    portfolioFiltre = PortfolioFiltre.objects.all()
    return render(request, 'projet_2/back/backoffice.html', {'abouts': abouts, 'skills': skills, 'skills_bar': skills_bar, 'services': services, 'testimonials': testimonials, 'contact': contact, 'portfolio': portfolio, 'portfolioFiltre': portfolioFiltre})
