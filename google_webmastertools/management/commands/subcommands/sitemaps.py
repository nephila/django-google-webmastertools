# -*- coding: utf-8 -*-
import sys

from google_webmastertools.management.commands.subcommands.base import SubcommandsCommand
from django.core.management.base import CommandError
from google_webmastertools import api
from gdata.webmastertools.data import SitemapEntry


class AddSitemapCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.sitemaps.sitemap_add``
    """
    args = 'sitemap-uri [sitemap-type]'
    help = 'Register a sitemap. Sitemap URI is either a relative URL or a valid urlconf name'

    def handle(self, *args, **options):
        try:
            type = 'WEB'
            sitemap = args[0]
            if len(args) > 1:
                type = args[1]
        except IndexError:
            raise CommandError("Not enough arguments. At least sitemap URI must be provided")
        status = api.sitemaps.sitemap_add(sitemap, type)
        if status.error:
            raise CommandError(status.error_message)
        else:
            self.stdout.write("Sitemap added for %s\n" %
                              status.domain)


class DeleteteSitemapCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.sitemaps.sitemap_delete``
    """
    args = 'sitemap-uri'
    help = 'Remove a sitemap. Sitemap URI is either a relative URL or a valid urlconf name'

    def handle(self, *args, **options):
        try:
            sitemap = args[0]
        except IndexError:
            raise CommandError("Not enough arguments. Sitemap URI must be provided")
        status = api.sitemaps.sitemap_delete(sitemap)

        if status.error:
            raise CommandError(status.error_message)
        else:
            self.stdout.write("Sitemap removed for %s\n" %
                              status.domain)


class ListSitemapCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.sitemaps.sitemap_list``
    """
    help = 'Get sitemaps list'

    def handle(self, *args, **options):
        status = api.sitemaps.sitemap_list()

        if status.error:
            raise CommandError(unicode(status))
        else:
            self.stdout.write(unicode(status))


class StatsSitemapCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.sitemaps.sitemap_stats``
    """
    args = 'sitemap-uri'
    help = 'Get sitemap stats. Sitemap URI is either a relative URL or a valid urlconf name'

    def handle(self, *args, **options):
        try:
            sitemap = args[0]
        except IndexError:
            raise CommandError("Not enough arguments. Sitemap URI must be provided")
        status = api.sitemaps.sitemap_stats(sitemap)

        if status.error:
            raise CommandError(unicode(status))
        else:
            self.stdout.write(unicode(status))

