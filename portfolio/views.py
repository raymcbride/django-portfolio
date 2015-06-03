# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from portfolio.models import Artifact, Category, Project


class CategoryList(ListView):

    context_object_name = 'category_list'
    template_name = 'portfolio/category_list.html'

    def get_queryset(self):
        return Category.objects.all()

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(CategoryList, self).dispatch(request, *args, **kwargs)
        except TemplateDoesNotExist:
            raise Http404


class CategoryDetail(DetailView):

    context_object_name = 'category'
    template_name = 'portfolio/category_detail.html'

    def get_object(self):
        return get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(CategoryDetail, self).dispatch(request, *args,
                                                        **kwargs)
        except TemplateDoesNotExist:
            raise Http404


class ProjectList(ListView):

    context_object_name = 'project_list'
    template_name = 'portfolio/project_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        return Project.objects.filter(category=self.category).filter(
            published=True)

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(ProjectList, self).dispatch(request, *args, **kwargs)
        except TemplateDoesNotExist:
            raise Http404


class ProjectDetail(DetailView):

    context_object_name = 'project'
    template_name = 'portfolio/project_detail.html'

    def get_object(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        return get_object_or_404(Project, category=self.category,
                                 published=True, slug=self.kwargs.get(
                                     'project_slug', ''))

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(ProjectDetail, self).dispatch(request, *args,
                                                       **kwargs)
        except TemplateDoesNotExist:
            raise Http404


class ArtifactList(ListView):

    context_object_name = 'artifact_list'
    template_name = 'portfolio/artifact_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        self.project = get_object_or_404(Project, category=self.category,
                                         published=True, slug=self.kwargs.get(
                                             'project_slug', ''))
        return Artifact.objects.filter(project=self.project).filter(
            published=True)

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(ArtifactList, self).dispatch(request, *args, **kwargs)
        except TemplateDoesNotExist:
            raise Http404


class ArtifactDetail(DetailView):

    context_object_name = 'artifact'
    template_name = 'portfolio/artifact_detail.html'

    def get_object(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(
            'category_slug', ''))
        self.project = get_object_or_404(Project, category=self.category,
                                         published=True, slug=self.kwargs.get(
                                             'project_slug', ''))
        return get_object_or_404(Artifact, project=self.project,
                                 published=True,
                                 slug=self.kwargs.get('artifact_slug', ''))

    def dispatch(self, request, *args, **kwargs):
        try:
            get_template(self.template_name)
            return super(ArtifactDetail, self).dispatch(request, *args,
                                                        **kwargs)
        except TemplateDoesNotExist:
            raise Http404
