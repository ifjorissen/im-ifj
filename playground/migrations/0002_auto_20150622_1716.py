# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playground.models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='motivation',
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to=playground.models.thumbnail_image_path, null=True),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='projimg',
            field=models.ImageField(upload_to=playground.models.image_path, null=True),
        ),
    ]
