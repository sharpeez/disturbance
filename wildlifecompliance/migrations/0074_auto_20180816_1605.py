# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-16 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0073_application_licence_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='lodgement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]