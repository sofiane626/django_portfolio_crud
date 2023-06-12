"""
URL configuration for projet_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import *
from about.views import *
from skills.views import *
from services.views import *
from testimonials.views import *
from contact.views import *
from portfolio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('About/edit', update, name='About_edit'),
    path('Skills/edit', updateSkills, name='Skills_edit'),
    path('Skills_bar/edit', updateSkills_bar, name='Skills_bar_edit'),
    path('home/', homepage),
    path('backoffice/', backoffice, name='backoffice'),
    path('create/skills_bar/', createSkills_bar, name='create_Skills_bar'),
    path('skills_bar/destroy/<int:id>', destroy_Skills),
    path('skills_bar/edit/<int:id>', updateSkills_bar),
    path('skills/', skills, name='skills'),
    path('services/', services, name='services'),
    path('services/destroy/<int:id>', destroy_Services),
    path('services/edit/<int:id>', updateServices),
    path('create/services/', createServices, name='create_Testimonials'),
    path('testimonials/', testimonials, name='Testimonials'),
    path('testimonials/destroy/<int:id>', destroy_Testimonials),
    path('testimonials/edit/<int:id>', updateTestimonials),
    path('create/testimonials/', createTestimonials, name='create_Testimonials'),
    path('Contact/edit', Contactupdate, name='Contact_edit'),
    path('Portfolio/', getPortfolio, name='Portfolio'),
    path('Portfolio/destroy/<int:id>', destroyPortfolio),
    path('portfolio/edit/<int:id>', updatePortfolio),
    path('create/portfolio/', createPortfolio, name='create_Portfolio'),
    path('PortfolioFiltre/destroy/<int:id>', destroyFiltre),
    path('portfolioFiltre/edit/<int:id>', updateFiltre),
    path('create/portfolioFiltre/', createFiltre, name='create_Filtre'),
]
