# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from portfolio.models import Artifact, Category, Project


class ProjectList(ListView):

    context_object_name = 'project_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        return Project.objects.filter(category=self.category).filter(
            published=True)


class ProjectDetail(DetailView):

    context_object_name = 'project'

    def get_object(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        return get_object_or_404(Project, category=self.category,
                                 published=True, slug=self.kwargs.get(
                                     'project_slug', ''))


class ArtifactList(ListView):

    context_object_name = 'artifact_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        self.project = get_object_or_404(Project, category=self.category,
                                         published=True, slug=self.kwargs.get(
                                             'project_slug', ''))
        return Artifact.objects.filter(project=self.project).filter(
            published=True)


class ArtifactDetail(DetailView):

    context_object_name = 'artifact'

    def get_object(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        self.project = get_object_or_404(Project, category=self.category,
                                         published=True, slug=self.kwargs.get(
                                             'project_slug', ''))
        return get_object_or_404(Artifact, project=self.project,
                                 published=True,
                                 slug=self.kwargs.get('artifact_slug', ''))
