# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
