# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.template import Context, Template
from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from portfolio.admin import ImageArtifactInline
from portfolio.factories import (CategoryFactory, FileArtifactFactory,
                                 ImageArtifactFactory, ProjectFactory,
                                 TextArtifactFactory)
from portfolio.models import (Category, FileArtifact, ImageArtifact, Project,
                              TextArtifact)
from portfolio.templatetags.portfolio_tags import get_artifact_list


class PortfolioModelsTests(TestCase):
    def setUp(self):
        super(PortfolioModelsTests, self).setUp()
        category = CategoryFactory()
        project = ProjectFactory(category=category)
        FileArtifactFactory(project=project)
        ImageArtifactFactory(project=project)
        TextArtifactFactory(project=project)

    def test___str__(self):
        project = Project.objects.get(slug='my-first-website')
        self.assertEqual(str(project), project.title)


class PortfolioViewsTests(TestCase):

    def setUp(self):
        super(PortfolioViewsTests, self).setUp()
        category = CategoryFactory()
        project = ProjectFactory(category=category)
        FileArtifactFactory(project=project)
        ImageArtifactFactory(project=project)
        TextArtifactFactory(project=project)

    def test_project_list(self):
        category = Category.objects.get(slug='my-websites')
        url = reverse('project_list', kwargs={'category_slug': category.slug})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        kwargs = {'category_slug': 'my-artwork'}
        url = reverse('project_list', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_project_detail_and_artifact_list(self):
        category = Category.objects.get(slug='my-websites')
        project = Project.objects.get(slug='my-first-website')
        kwargs = {'category_slug': category.slug, 'project_slug': project.slug}
        url = reverse('project_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        url = reverse('artifact_list', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        kwargs = {'category_slug': 'my-artwork', 'project_slug': project.slug}
        url = reverse('project_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        url = reverse('artifact_list', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        kwargs = {'category_slug': category.slug, 'project_slug': 'my-project'}
        url = reverse('project_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        url = reverse('artifact_list', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_artifact_detail(self):
        category = Category.objects.get(slug='my-websites')
        project = Project.objects.get(slug='my-first-website')
        image_artifact = ImageArtifact.objects.get(slug='an-image')
        url = reverse('artifact_detail',
                      kwargs={'category_slug': category.slug,
                              'project_slug': project.slug,
                              'artifact_slug': image_artifact.slug})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        kwargs = {'category_slug': 'my-artwork', 'project_slug': project.slug,
                  'artifact_slug': image_artifact.slug}
        url = reverse('artifact_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        kwargs = {'category_slug': category.slug, 'project_slug': 'my-project',
                  'artifact_slug': image_artifact.slug}
        url = reverse('artifact_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        kwargs = {'category_slug': category.slug, 'project_slug': project.slug,
                  'artifact_slug': 'another-image'}
        url = reverse('artifact_detail', kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)


class PortfolioTemplateTagsTests(TestCase):

    TEMPLATE = Template('{% load portfolio_tags %} \
                       {{"*This is the description*"|convert_markdown|safe }}')

    def setUp(self):
        super(PortfolioTemplateTagsTests, self).setUp()
        category = CategoryFactory()
        project = ProjectFactory(category=category)
        FileArtifactFactory(project=project)
        ImageArtifactFactory(project=project)
        TextArtifactFactory(project=project)

    def test_get_artifact_list(self):
        project = Project.objects.get(slug='my-first-website')
        image_artifact = ImageArtifact.objects.get(slug='an-image')
        file_artifact = FileArtifact.objects.get(slug='a-file')
        text_artifact = TextArtifact.objects.get(slug='text')
        artifact_list = get_artifact_list(Context({'project': project}))
        self.assertEqual(len(artifact_list), 3)
        artifact_list = get_artifact_list(Context({'project': project}),
                                          artifact_type="image")
        self.assertIn(image_artifact, artifact_list)
        artifact_list = get_artifact_list(Context({'project': project}),
                                          artifact_type="file")
        self.assertIn(file_artifact, artifact_list)
        artifact_list = get_artifact_list(Context({'project': project}),
                                          artifact_type="text")
        self.assertIn(text_artifact, artifact_list)
        artifact_list = get_artifact_list(Context({'project': project}),
                                          artifact_type="blob")
        self.assertEqual(len(artifact_list), 0)

    def test_convert_markdown(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertHTMLEqual(rendered,
                             '<p><em>This is the description</em></p>')


class PortfolioAdminTests(TestCase):

    def setUp(self):
        super(PortfolioAdminTests, self).setUp()
        category = CategoryFactory()
        project = ProjectFactory(category=category)
        FileArtifactFactory(project=project)
        ImageArtifactFactory(project=project)
        TextArtifactFactory(project=project)

    def test_image_thumb(self):
        image_artifact_inline = ImageArtifactInline(ImageArtifact, AdminSite())
        image_artifact = ImageArtifact.objects.get(slug='an-image')
        self.assertHTMLEqual(ImageArtifactInline.image_thumb(
                             image_artifact_inline, image_artifact),
                             '<img src="%s" width="250" />' %
                             image_artifact.image.url)
