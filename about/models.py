from django.db import models

# Create your models here.


class About(models.Model):
    paragraphe1 = models.TextField()
    birthday = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phEmailone = models.CharField(max_length=100)
    freelance = models.CharField(max_length=100)
    paragraphe2 = models.TextField()
