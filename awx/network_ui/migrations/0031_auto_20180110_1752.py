# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 17:52
from __future__ import unicode_literals

from django.db import migrations

results = ['passed',
           'failed',
           'errored',
           'skipped',
           'aborted',
           'not run',
           'blocked']

def populate_result_types(apps, schema_editor):

    Result = apps.get_model('network_ui', 'Result')
    for result in results:
        Result.objects.get_or_create(name=result)


class Migration(migrations.Migration):

    dependencies = [
        ('network_ui', '0030_auto_20180110_1751'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_result_types,
        ),
    ]