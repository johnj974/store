# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-07 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200401_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='horsepower',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='manufacturer',
            new_name='size',
        ),
    ]
