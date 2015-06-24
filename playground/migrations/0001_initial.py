# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added to site')),
                ('projurl', models.URLField()),
                ('completion_date', models.DateTimeField(verbose_name='date completed')),
                ('objective', models.TextField()),
                ('description', models.TextField()),
                ('motivation', models.TextField()),
                ('solution', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectColor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('hexa', models.TextField(max_length=10)),
                ('project', models.ForeignKey(null=True, to='playground.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('caption', models.TextField()),
                ('projimg', models.ImageField(null=True, upload_to='playground/%Y/%m/%d')),
                ('proj', models.ForeignKey(null=True, to='playground.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTech',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('project', models.ForeignKey(null=True, to='playground.Project')),
            ],
        ),
    ]
