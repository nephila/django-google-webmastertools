# -*- coding: utf-8 -*-
import os.path
import sys
import codecs

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from google_webmaster.management.commands.subcommands.base import SubcommandsCommand
from google_webmaster import api


class CheckCommand(SubcommandsCommand):
    #args = 'metatag|htmlpage'
    help = 'Check if site is registered and verified'

    def handle(self, *args, **options):
        status = api.base.check_domain()
        if status.error:
            raise CommandError('Site %s not registered in Webmaster tools' %
                               status.domain)
        elif not status.verified:
            raise CommandError('Site %s registered in Webmaster tools but not verified' %
                               status.domain)
        else:
            self.stdout.write("Site %s registered in Webmaster tools and verified\n" %
                              status.domain)

