# -*- coding: utf-8 -*-
import os.path
import sys
import codecs

from django.conf import settings
from gdata.webmastertools.service import GWebmasterToolsService
from gdata.webmastertools import *
from google_webmastertools.api.base import _get_domain, get_client, StatusObject
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.defaultfilters import urlencode
from gdata.webmastertools.data import SitemapEntry
from .url import KEYWORDS_FEED


def keywords_list(domain=None):
    """ Lists keywords as reported by the API.
    """
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)

    def pretty(status):
        text = u"\n".join(status.entry)
        return text

    try:
        url = KEYWORDS_FEED % {"siteid":siteid}
        entry = client.Get(url)
        keywords = []
        for k in entry.FindExtensions():
            keywords.append(unicode(k.text))
        status.error = False
        status.entry = keywords
        status.pretty_print = pretty
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status
