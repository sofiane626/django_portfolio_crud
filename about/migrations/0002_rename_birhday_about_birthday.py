# Generated by Django 4.2.1 on 2023-06-06 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='birhday',
            new_name='birthday',
        ),
    ]