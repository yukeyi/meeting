# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-30 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_userlogin_my_conf'),
    ]

    operations = [
        migrations.AddField(
            model_name='confbasic',
            name='money',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
