# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_farm_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='unit',
            field=models.IntegerField(),
        ),
    ]
