# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-01 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date'),
        ),
    ]
