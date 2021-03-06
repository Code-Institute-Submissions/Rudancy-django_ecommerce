# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-20 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200520_1135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.CharField(choices=[('M', 'Mens'), ('F', 'Women'), ('k', 'kids')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('AD', 'Addidas'), ('NK', 'Nike'), ('CV', 'Coverse'), ('DD', 'Diadora'), ('EA', 'Emporium Armani'), ('NB', 'New Balance'), ('PM', 'Puma')], default='', max_length=20),
        ),
    ]
