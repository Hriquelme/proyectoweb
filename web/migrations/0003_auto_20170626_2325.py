# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170626_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada2',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
