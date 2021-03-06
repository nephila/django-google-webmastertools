# -*- coding: utf-8 -*-
import os.path
import sys
import codecs

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from google_webmastertools.management.commands.subcommands.base import SubcommandsCommand
from google_webmastertools import api


class CheckCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.base.check_domain``
    """
    help = 'Check if site is registered and verified'

    def handle(self, *args, **options):
        status = api.base.check_domain()
        if status.error:
            raise CommandError(status.error_message)
        elif not status.verified:
            raise CommandError('Site %s registered in Webmaster tools but not verified' %
                               status.domain)
        else:
            self.stdout.write("Site %s registered in Webmaster tools and verified\n" %
                              status.domain)


class AddCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.base.add_domain``
    """
    help = 'Register a domain'

    def handle(self, *args, **options):
        status = api.base.add_domain()
        if status.error:
            raise CommandError(status.error_message)
        else:
            self.stdout.write("Site %s registered in Webmaster tools, please verify it\n" %
                              status.domain)


class VerifyCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.base.verifiy_domain``
    """
    help = 'Verify a using htmlpage'

    def handle(self, *args, **options):
        status = api.base.verify_domain()
        if status.error:
            raise CommandError(status.error_message)
        else:
            self.stdout.write("Site %s verified in Webmaster tools\n" %
                              status.domain)


class DeleteCommand(SubcommandsCommand):
    """ Wrapper for ``google_webmastertools.api.base.delete_domain``
    """
    help = 'Unregister a domain'

    def handle(self, *args, **options):
        status = api.base.delete_domain()
        if status.error:
            raise CommandError(status.error_message)
        else:
            self.stdout.write("Site %s unregistered Webmaster tools\n" %
                              status.domain)

