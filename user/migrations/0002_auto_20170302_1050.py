# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-02 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verify',
            options={'verbose_name': '用户验证', 'verbose_name_plural': '用户验证'},
        ),
    ]