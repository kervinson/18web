# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-01 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('active_code', models.CharField(max_length=40, verbose_name='验证码')),
            ],
        ),
    ]