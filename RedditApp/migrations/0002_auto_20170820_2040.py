# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 01:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedditApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 8, 21, 1, 40, 36, 347033, tzinfo=utc)),
        ),
    ]
