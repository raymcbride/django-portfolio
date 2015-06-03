from django.conf.urls import patterns, url

from portfolio.views import (ArtifactDetail, ArtifactList, ProjectDetail,
                             ProjectList, CategoryDetail, CategoryList)

urlpatterns = patterns(
    '',
    url(r'^(?P<category_slug>[-\w]+)/projects/(?P<project_slug>[-\w]+)/pages/'
        '(?P<artifact_slug>[-\w]+)/$', ArtifactDetail.as_view(),
        name='artifact_detail'),
    url(r'^(?P<category_slug>[-\w]+)/projects/(?P<project_slug>[-\w]+)/'
        'pages/$', ArtifactList.as_view(), name='artifact_list'),
    url(r'^(?P<category_slug>[-\w]+)/projects/(?P<project_slug>[-\w]+)/$',
        ProjectDetail.as_view(), name='project_detail'),
    url(r'^(?P<category_slug>[-\w]+)/projects/$', ProjectList.as_view(),
        name='project_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', CategoryDetail.as_view(),
        name='category_detail'),
    url(r'^$', CategoryList.as_view(),
        name='category_list'),

)
