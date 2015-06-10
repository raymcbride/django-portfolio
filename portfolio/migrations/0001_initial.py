# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(help_text='<a href="http://en.wikipedia.org/wiki/Markdown">Markdown</a> formatting available')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileArtifact',
            fields=[
                ('artifact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.Artifact')),
                ('file', models.FileField(upload_to='portfolio/files/')),
            ],
            options={
            },
            bases=('portfolio.artifact',),
        ),
        migrations.CreateModel(
            name='ImageArtifact',
            fields=[
                ('artifact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.Artifact')),
                ('image', models.ImageField(upload_to='portfolio/images/')),
            ],
            options={
            },
            bases=('portfolio.artifact',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(help_text='<a href="http://en.wikipedia.org/wiki/Markdown">Markdown</a> formatting available')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('date_completed', models.DateField(null=True, blank=True)),
                ('category', models.ForeignKey(related_name='projects', to='portfolio.Category')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextArtifact',
            fields=[
                ('artifact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.Artifact')),
                ('content', models.TextField(help_text='<a href="http://en.wikipedia.org/wiki/Markdown">Markdown</a> formatting available')),
            ],
            options={
            },
            bases=('portfolio.artifact',),
        ),
        migrations.AddField(
            model_name='artifact',
            name='project',
            field=models.ForeignKey(related_name='artifacts', to='portfolio.Project'),
            preserve_default=True,
        ),
    ]
