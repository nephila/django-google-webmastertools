# -*- coding: utf-8 -*-
import os.path
import sys
import codecs

from django.conf import settings
from gdata.webmastertools.service import GWebmasterToolsService
from gdata.webmastertools import *
from django.contrib.sites.models import Site
from django.template.defaultfilters import urlencode
from .url import CHECK_URL


class StatusObject(object):
    """ StatusObject encapsulate a tiny logic to adapt messages returned by API
    """
    error = True
    error_message = ""
    verified = False
    domain = ""
    entry = None

    def __init__(self, domain, error=True, error_message="", verified=False):
        self.domain = domain
        self.error = error
        self.error_message = error_message
        self.verified = verified

    def __unicode__(self):
        if self.error and self.error_message:
            return self.error_message
        elif hasattr(self, 'pretty_print'):
            return self.pretty_print(self)
        elif self.entry:
            return unicode(self.entry)
        else:
            return self.error


def get_client():
    """ Opens a connection to Google API and returns the client instance
    """
    client = GWebmasterToolsService(settings.GOOGLE_WEBMASTERTOOLS_LOGIN,
                                    settings.GOOGLE_WEBMASTERTOOLS_PASSWORD)
    client.email = settings.GOOGLE_WEBMASTERTOOLS_LOGIN
    client.password = settings.GOOGLE_WEBMASTERTOOLS_PASSWORD
    client.ProgrammaticLogin()
    return client


def _get_domain(domain=None):
    """ Create domain string from Django Site object needed by Google API
    """
    if not domain:
        domain = Site.objects.get_current().domain
    if domain.find("http") == -1:
        domain = "http://" + domain + "/"
    siteid = urlencode(domain).replace(".", "%2E").replace("/", "%2F")
    return (domain, siteid)


def add_domain(domain=None):
    """ Add a domain to Webmaster Tools

    Opens its own connection to API
    """
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)

    try:
        entry = client.AddSite(domain)
        status.error = False
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def verify_domain(domain=None):
    """ Verify a domain to Webmaster Tools

    Triggers Webmaster Tools into starting a domain verification using HTML page
    """
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)

    try:
        entry = client.VerifySite(domain, "htmlpage")
        status.error = False
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def delete_domain(domain=None):
    """ Delete a domain to Webmaster Tools

    Deletes a domain from Webmaster tools account. Does not require *any*
    confirmation
    """
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)

    try:
        entry = client.DeleteSite(domain)
        if entry:
            status.error = False
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def check_domain(domain=None):
    """ Check if domain is already registered in Webmaster Tools
    """
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)
    try:
        f = client.GetEntry("%s%s" % (CHECK_URL, siteid))
        g = SitesEntryFromString(str(f))
        if g.verified.text == "false":
            status.error = False
        else:
            status.error = False
            status.verified = True
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status