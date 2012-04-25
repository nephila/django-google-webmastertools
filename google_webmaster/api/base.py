# -*- coding: utf-8 -*-
import os.path
import sys
import codecs

from django.conf import settings
from gdata.webmastertools.service import GWebmasterToolsService
from gdata.webmastertools import *
from django.contrib.sites.models import Site
from django.template.defaultfilters import urlencode


class StatusObject(object):
    error = True
    error_message = ""
    verified = False
    domain = ""

    def __init__(self, domain, error=True, error_message="", verified=False):
        self.domain = domain
        self.error = error
        self.error_message = error_message
        self.verified = verified


def get_client():
    client = GWebmasterToolsService(settings.GOOGLE_WEBMASTERTOOLS_LOGIN,
                                    settings.GOOGLE_WEBMASTERTOOLS_PASSWORD)
    client.email = settings.GOOGLE_WEBMASTERTOOLS_LOGIN
    client.password = settings.GOOGLE_WEBMASTERTOOLS_PASSWORD
    client.ProgrammaticLogin()
    return client


def check_domain(domain=None):
    if not domain:
        domain = Site.objects.get_current().domain
    siteid = urlencode("http://" + domain + "/").replace(".", "%2E").replace("/", "%2F")
    client = get_client()
    status = StatusObject(domain)
    try:
        f = client.GetEntry("https://www.google.com/webmasters/tools/feeds/sites/" + siteid)
        g = SitesEntryFromString(str(f))
        if g.verified.text == "false":
            status.error = False
        else:
            status.error = False
            status.verified = True
    except gdata.service.RequestError:
        status.error_message = 'Site %s not registered in Webmaster tools'
    return status
