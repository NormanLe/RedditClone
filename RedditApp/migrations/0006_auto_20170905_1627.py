# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 21:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RedditApp', '0005_auto_20170901_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs', models.ManyToManyField(to='RedditApp.Subblueit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 9, 5, 21, 27, 0, 533380, tzinfo=utc)),
        ),
    ]
