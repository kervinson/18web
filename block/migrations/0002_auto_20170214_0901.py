# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-14 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='板块描述'),
        ),
        migrations.AlterField(
            model_name='block',
            name='manager',
            field=models.CharField(max_length=100, verbose_name='管理员名称'),
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(max_length=100, verbose_name='板块名称'),
        ),
    ]