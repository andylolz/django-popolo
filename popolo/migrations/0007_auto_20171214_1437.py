# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popolo', '0006_auto_20171212_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='code',
            field=models.CharField(blank=True, help_text='An alphanumerical code in use within the scheme', max_length=128, null=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='descr',
            field=models.CharField(blank=True, help_text='The extended, textual description of the classification', max_length=512, null=True, verbose_name='description'),
        ),
    ]
