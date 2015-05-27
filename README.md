#django-portfolio

A simple Django portfolio app.

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

The following templates are required by django-portfolio, so you'll need to create them:
