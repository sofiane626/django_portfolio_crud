# Generated by Django 4.2.1 on 2023-06-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=100)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.CharField(max_length=100)),
            ],
        ),
    ]
