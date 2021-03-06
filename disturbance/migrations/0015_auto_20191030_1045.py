# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-30 02:45
from __future__ import unicode_literals

import disturbance.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0014_auto_20191030_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='admin_pin_one',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='organisation',
            name='admin_pin_two',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='organisation',
            name='user_pin_one',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='organisation',
            name='user_pin_two',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=500, upload_to=disturbance.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]
