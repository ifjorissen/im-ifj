# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
