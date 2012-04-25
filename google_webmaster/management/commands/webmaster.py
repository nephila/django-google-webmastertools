# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .subcommands.base import SubcommandsCommand
from .subcommands.check import CheckCommand
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(SubcommandsCommand):

    args = '<subcommand>'

    command_name = 'webmaster'

    subcommands = {
        'check': CheckCommand,
    }

    @property
    def help(self):
        lines = ['Google Webmaster tools command line interface for Django.', '', 'Available subcommands:']
        for subcommand in sorted(self.subcommands.keys()):
            lines.append('  %s' % subcommand)
        lines.append('')
        lines.append('Use `manage.py webmaster <subcommand> --help` for help about subcommands')
        return '\n'.join(lines)
