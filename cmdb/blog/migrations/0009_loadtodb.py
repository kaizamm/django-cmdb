# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170428_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadToDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadtodb', models.FileField(blank=True, upload_to='uploads/')),
            ],
        ),
    ]
