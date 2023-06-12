from django.db import models

# Create your models here.


class Services(models.Model):
    logo = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    contenu = models.CharField(max_length=100)
