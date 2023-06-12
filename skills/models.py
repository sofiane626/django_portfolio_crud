from django.db import models

# Create your models here.


class Skills(models.Model):
    paragraphe3 = models.TextField()


class Skills_bar(models.Model):
    texte_progression = models.CharField(max_length=100)
    progression = models.IntegerField(default=0)
