# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

import factory

from portfolio.models import (Category, FileArtifact, ImageArtifact, Project,
                              TextArtifact)


class CategoryFactory(factory.django.DjangoModelFactory):
    title = 'My Websites'
    slug = 'my-websites'

    class Meta:
        model = Category


class ProjectFactory(factory.django.DjangoModelFactory):
    title = 'My First Website'
    slug = 'my-first-website'
    description = '*This is the description*'
    published = True
    date_completed = datetime.datetime.now()

    class Meta:
        model = Project


class FileArtifactFactory(factory.django.DjangoModelFactory):
    title = 'A File'
    slug = 'a-file'
    order = 0
    description = 'File Description'
    published = True
    file = factory.django.FileField(filename='foo.txt')

    class Meta:
        model = FileArtifact


class ImageArtifactFactory(factory.django.DjangoModelFactory):
    title = 'An Image'
    slug = 'an-image'
    order = 0
    description = 'Image Description'
    published = True
    image = factory.django.ImageField(filename='bar.jpg')

    class Meta:
        model = ImageArtifact


class TextArtifactFactory(factory.django.DjangoModelFactory):
    title = 'Text'
    slug = 'text'
    order = 0
    description = 'Text Description'
    published = True
    content = 'This is the content'

    class Meta:
        model = TextArtifact
