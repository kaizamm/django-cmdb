# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdbinfo',
            name='area',
            field=models.CharField(choices=[('IDC', 'IDC'), ('SH', 'SH'), ('WH', 'WH')], default='IDC', max_length=3),
        ),
        migrations.AlterField(
            model_name='cmdbinfo',
            name='os',
            field=models.CharField(choices=[('Centos7', 'Centos7'), ('Centos6', 'Centos6'), ('Windows', 'Windows')], default='Centos7', max_length=250),
        ),
    ]
