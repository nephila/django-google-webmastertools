# -*- coding: utf-8 -*-
from django.http import HttpResponse


def verification(request, siteid=None):
    return HttpResponse("google-site-verification: %s.html" % siteid,
                        mimetype="text/plain")
