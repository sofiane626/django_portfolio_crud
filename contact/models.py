from django.db import models

# Create your models here.


class Contact(models.Model):
    location = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
