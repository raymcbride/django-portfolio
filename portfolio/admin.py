# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from portfolio.models import (Category, FileArtifact, ImageArtifact, Project,
                              TextArtifact)


class ArtifactInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('title',)}


class ImageArtifactInline(ArtifactInline):
    model = ImageArtifact
    extra = 1
    readonly_fields = ('image_thumb',)

    def image_thumb(self, obj):
        return '<img src="%s" width="250" />' % (obj.image.url)

    image_thumb.allow_tags = True


class FileArtifactInline(ArtifactInline):
    model = FileArtifact
    extra = 1


class TextArtifactInline(ArtifactInline):
    model = TextArtifact
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_completed', 'published')
    list_filter = ('category', 'published')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (
        ImageArtifactInline,
        FileArtifactInline,
        TextArtifactInline,
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
