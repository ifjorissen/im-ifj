# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playground.models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_auto_20150619_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=playground.models.thumbnail_image_path),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='projimg',
            field=models.ImageField(null=True, upload_to=playground.models.image_path),
        ),
    ]
