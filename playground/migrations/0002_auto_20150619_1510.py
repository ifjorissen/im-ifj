# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
            field=models.ForeignKey(to='playground.ProjectImage', null=True),
        ),
    ]
