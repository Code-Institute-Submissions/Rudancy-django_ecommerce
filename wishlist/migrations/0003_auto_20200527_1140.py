# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-27 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200524_1409'),
        ('wishlist', '0002_wish_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish_list',
            name='wished_product',
        ),
        migrations.AddField(
            model_name='wish_list',
            name='wished_product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
