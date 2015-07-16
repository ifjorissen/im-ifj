# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='objective',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projurl',
            field=models.URLField(null=True, blank=True),
        ),
    ]
