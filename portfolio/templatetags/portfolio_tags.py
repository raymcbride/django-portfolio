# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django import template

from portfolio.models import (Artifact, FileArtifact, ImageArtifact,
                              TextArtifact)

register = template.Library()


@register.assignment_tag()
def get_artifact_list(project, artifact_type=""):
    if artifact_type == "":
        return Artifact.objects.filter(project=project) \
            .filter(published=True)
    elif artifact_type == "file":
        return FileArtifact.objects.filter(project=project) \
            .filter(published=True)
    elif artifact_type == "image":
        return ImageArtifact.objects.filter(project=project) \
            .filter(published=True)
    elif artifact_type == "text":
        return TextArtifact.objects.filter(project=project) \
            .filter(published=True)
    else:
        return []


@register.filter
def convert_markdown(text):
    return markdown.markdown(text, safe_mode='escape')
