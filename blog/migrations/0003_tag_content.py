# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150704_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='content',
            field=models.CharField(max_length=200, unique=True, default=None),
        ),
    ]
