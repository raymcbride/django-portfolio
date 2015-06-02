# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

MARKDOWN_HELP_TEXT = '' \
    '<a href="http://en.wikipedia.org/wiki/Markdown">Markdown</a> ' \
    'formatting available'


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(help_text=MARKDOWN_HELP_TEXT)
    published = models.BooleanField('Published', default=False)
    date_completed = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='projects')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'project_detail',
            kwargs={
                'category_slug': self.category.slug,
                'project_slug': self.slug
            }
        )


class Artifact(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.IntegerField(null=True, blank=True)
    description = models.TextField(help_text=MARKDOWN_HELP_TEXT)
    project = models.ForeignKey(Project, related_name='artifacts')
    published = models.BooleanField('Published', default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'artifact_detail',
            kwargs={
                'category_slug': self.project.category.slug,
                'project_slug': self.project.slug,
                'artifact_slug': self.slug
            }
        )


class FileArtifact(Artifact):
    file = models.FileField(upload_to='portfolio/files/')


class ImageArtifact(Artifact):
    image = models.ImageField(upload_to='portfolio/images/')


class TextArtifact(Artifact):
    content = models.TextField(help_text=MARKDOWN_HELP_TEXT)
