from django.db import models

# Create your models here.


class PortfolioFiltre(models.Model):
    filtre = models.CharField(max_length=100)


class Portfolio(models.Model):
    img = models.CharField(max_length=100)
    choixFiltre = models.CharField(max_length=100)
