django-google-webmastertools
============================

django-google-webmastertools is a set of Django commands to work with Google's
Webmaster Tools (GWT from now on) to handle the basic chores of setting up and
managing a site profile on GWT.
Unfortunately GWT API is far from complete, and it only covers a few basic
actions.
django-google-webmastertools plans to do its best to implement it.


Installation
************
django-google-webmastertools it's not on pypi at the moment,but you can install
it from github with ``pip``::

    $ pip install -e https://github.com/nephila/django-google-webmastertools.git#egg=django-google-webmastertools


Configuration
*************
You need to configure a GWT account using ``GOOGLE_WEBMASTERTOOLS_LOGIN`` and
``GOOGLE_WEBMASTERTOOLS_PASSWORD`` variable::

    GOOGLE_WEBMASTERTOOLS_LOGIN = "whatever@gmail.com"
    GOOGLE_WEBMASTERTOOLS_PASSWORD = "very-secret-password"

Then add ``google_webmastertools`` to your INSTALLED_APPS

For ``verify`` command to work you have to set proper url pattern in urlconf::

    from google_webmastertools.utils import verification
    ...
    (r'^(?P<siteid>google[0-9a-z]+)\.html$', verification),

this way every request to verification-style pages will be handled accordingly.

Commands
********
Command structure is mostly derived from django-cms' one: thanks to Divio
for it.
While code looks a little weird, it serves the purpose to not clutter
manage.py with too many commands.

Implemented commands
--------------------
Commands are called from command line prepending *webmaster* command with
is the basic dispatch command::

    python manage.py webmaster command [options] 

All the commands operate on the domain configured in django site; at the
moment only one-site-projects are supported, while multi-site is planned
for a not distant future.


check
#####
Check if domain is registered in GWT.

add
###
Add the domain to GWT; this command does not verify the site.
``verify`` subcommand does that *after* site has been added.

delete
######
*Completely removes* site from GWT.

verify
######
Verify site ownership via htmlfile. Please see ``Installation`` to see
how to configure urlconf for this command to work.

sitemap_add
###########
Submit a sitemap; it's developer responsibility to actually build a sitemap,
either by hand or by coding using any of the supported Django methods.
Sitemap URL o urlconf name is required::

    python manage.py webmaster sitemap_add '/sitemap.xml'

sitemap_delete
##############
Removes a sitemap.
Sitemap URL o urlconf name is required::

    python manage.py webmaster sitemap_delete '/sitemap.xml'

sitemap_stats
#############
Return available sitemap stats. GWT API does not return much data, at the end
it's useful just for checking and debugging purposes.
Sitemap URL o urlconf name is required::

    python manage.py webmaster sitemap_stats '/sitemap.xml'


sitemap_list
############
List all the sitemaps registered.


keywords_list
#############
Just return keyword list, due to API restrictions. Useful for debugging
definitely not for content analisys.
