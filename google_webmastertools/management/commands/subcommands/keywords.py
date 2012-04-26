# -*- coding: utf-8 -*-
import sys

from google_webmastertools.management.commands.subcommands.base import SubcommandsCommand
from django.core.management.base import CommandError
from google_webmastertools import api
from gdata.webmastertools.data import SitemapEntry


class ListKeywordsCommand(SubcommandsCommand):
    help = 'Get keywords list'

    def handle(self, *args, **options):
        status = api.keywords.keywords_list()

        if status.error:
            raise CommandError(unicode(status))
        else:
            self.stdout.write(unicode(status))

