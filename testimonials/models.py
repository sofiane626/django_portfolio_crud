from django.db import models

# Create your models here.


class Testimonials(models.Model):
    nom = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    citation = models.TextField()
