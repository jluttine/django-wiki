"""A set of context processors for Django-Wiki.

Each function takes the request object as its only parameter and returns
a dictionary to add to the context.
"""
from django.conf import settings


def breadcrumbs(request):
    """
    Adds breadcrumbs-related context variables to the context.
    """
    return {'WIKI_BREADCRUMBS_ROOT_LEVEL': getattr(settings, 'WIKI_BREADCRUMBS_ROOT_LEVEL', 0)}

