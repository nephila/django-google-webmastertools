# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .subcommands.base import SubcommandsCommand
from .subcommands.basic import *
from .subcommands.sitemaps import *
from .subcommands.keywords import *
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(SubcommandsCommand):

    args = '<subcommand>'

    command_name = 'webmaster'

    subcommands = {
        'check': CheckCommand,
        'add': AddCommand,
        'delete': DeleteCommand,
        'verify': VerifyCommand,
        'sitemap_add': AddSitemapCommand,
        'sitemap_delete': DeleteteSitemapCommand,
        'sitemap_stats': StatsSitemapCommand,
        'sitemap_list': ListSitemapCommand,
        'keywords_list': ListKeywordsCommand,
    }

    @property
    def help(self):
        lines = ['Google Webmaster tools command line interface for Django.', '', 'Available subcommands:']
        for subcommand in sorted(self.subcommands.keys()):
            lines.append('  %s' % subcommand)
        lines.append('')
        lines.append('Use `manage.py webmaster <subcommand> --help` for help about subcommands')
        return '\n'.join(lines)
