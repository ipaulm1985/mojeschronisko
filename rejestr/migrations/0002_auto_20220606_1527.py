# Generated by Django 3.0.10 on 2022-06-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pies_badania',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pies_dieta',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pies_leczenie',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]