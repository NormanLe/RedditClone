# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 19:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedditApp', '0004_auto_20170901_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 9, 1, 19, 2, 32, 809055, tzinfo=utc)),
        ),
    ]
