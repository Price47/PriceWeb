# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-08 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceweb', '0002_auto_20170908_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='television',
            name='search_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
