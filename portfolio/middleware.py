# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import TemplateDoesNotExist
from django.views.defaults import page_not_found


class TemplateDoesNotExistMiddleware(object):
    """
    If this is enabled, the middleware will catch TemplateDoesNotExist
    exceptions, and return a 404 response.
    """

    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            return page_not_found(request)
