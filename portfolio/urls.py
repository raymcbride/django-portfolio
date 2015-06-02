from django.conf.urls import patterns, url

from portfolio.views import (ArtifactDetail, ArtifactList, ProjectDetail,
                             ProjectList)

urlpatterns = patterns(
    '',
    url(r'^(?P<category_slug>[-\w]+)/(?P<project_slug>[-\w]+)/pages/'
        '(?P<artifact_slug>[-\w]+)/$', ArtifactDetail.as_view(),
        name='artifact_detail'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<project_slug>[-\w]+)/pages/$',
        ArtifactList.as_view(), name='artifact_list'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<project_slug>[-\w]+)/$',
        ProjectDetail.as_view(), name='project_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProjectList.as_view(),
        name='project_list'),
)
