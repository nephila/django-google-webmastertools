# -*- coding: utf-8 -*-
"""
Insert the view below in main urls.py adding this line:

(r'^(?P<siteid>google[0-9a-z]+)\.html$', verification),
"""
from django.http import HttpResponse

def verification(request, siteid=None):
    """ View that takes care of Webmaster Tools verification request
    """
    return HttpResponse("google-site-verification: %s.html" % siteid,
                        mimetype="text/plain")
