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
from .url import SITEMAP_FEED


def _sitemap_pretty_print(map):
    return "%s\n - # URL: %s\n - Last download: %s\n - Updated: %s\n" \
        % (map.title.text, map.sitemap_url_count.text,
          map.sitemap_last_downloaded.text, map.updated.text)


def _get_sitemap(sitemap, domain):
    try:
        sitemap = reverse(sitemap)
    except NoReverseMatch:
        pass
    sitemap = domain + sitemap[1:]
    sitemapid = urlencode(sitemap).replace(".", "%2E").replace("/", "%2F")
    return (sitemap, sitemapid)


def sitemap_stats(sitemap, domain=None):
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)
    sitemap, sitemapid = _get_sitemap(sitemap, domain)

    def pretty(status):
        return _sitemap_pretty_print(status.entry)

    try:
        url = SITEMAP_FEED % {"siteid":siteid, "sitemapid":sitemapid}
        entry = client.Get(url)
        g = atom.CreateClassFromXMLString(SitemapsEntry, str(entry))
        status.error = False
        status.entry = g
        status.pretty_print = pretty
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def sitemap_list(domain=None):
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)

    def pretty(status):
        text = ""
        text += "%s sitemaps\n" % len(status.entry.entry)
        text += "Last updated %s\n" % status.entry.updated.text
        for map in status.entry.entry:
            text += _sitemap_pretty_print(map)
        return text

    try:
        entry = client.GetSitemapsFeed(domain)
        status.error = False
        status.entry = entry
        status.pretty_print = pretty
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def sitemap_add(sitemap, sitemap_type, domain=None):
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)
    sitemap, sitemapid = _get_sitemap(sitemap, domain)

    try:
        entry = client.AddSitemap(domain, sitemap, sitemap_type)
        status.error = False
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status


def sitemap_delete(sitemap, domain=None):
    domain, siteid = _get_domain(domain)
    client = get_client()
    status = StatusObject(domain)
    sitemap, sitemapid = _get_sitemap(sitemap, domain)

    try:
        entry = client.DeleteSitemap(domain, sitemap)
        status.error = False
    except gdata.service.RequestError, e:
        status.error_message = e.message['body']
    return status