#django-portfolio

A simple Django portfolio app which allows you to create categorised projects. Each project can contain a series of resources called artifacts related to that project. Artifacts take the follow forms:

* image artifacts
* file artifacts
* text artifacts

[![Build
Status](https://travis-ci.org/raymcbride/django-portfolio.svg?branch=master)](https://travis-ci.org/raymcbride/django-portfolio)
[![Coverage
Status](https://coveralls.io/repos/raymcbride/django-portfolio/badge.svg)](https://coveralls.io/r/raymcbride/django-portfolio)

##Installation

Install using pip:

    $ pip install -e git+https://github.com/raymcbride/django-portfolio.git#egg=django-portfolio

Add to your INSTALLED_APPS setting:

    INSTALLED_APPS = (
        ...
        'portfolio',
        ...
     )

Include URLs in your project URLs:

    urlpatterns = patterns(
        '',
        (r'^portfolio/', include('portfolio.urls')),
        ...
    )

##Templates

The following templates are required by django-portfolio so you'll need to create them if you want to display the corresponding views. If you don't provide the specific template then the View will return a 404:

* portfolio/category_list.html - the template which renders the list of your categories
* portfolio/category_detail.html - the template which renders a category detail
* portfolio/project_list.html - the template which renders the list of your projects
* portfolio/project_detail.html - the template which renders a project detail
* portfolio/artifact_list.html - the template which renders the list of a project artifacts
* portfolio/artifact_detail.html - the template which renders an artifact detail

##Template Tags and Filters

To use these helpers load portfolio_tags into your template:

    {% load portfolio_tags %}

###get_artifact_list

This tag takes the context and an artifact_type string and returns a list
of published artifacts of that type for a specific project. The
artifact_type string can be one of the follow:

* "image"
* "file"
* "text"

####Usage

    {% get_artifact_list "image" as image_artifact_list %}

###convert_markdown

This filter converts a field containing markdown to HTML.

####Usage
 
    {{ project.description|convert_markdown|safe }}
