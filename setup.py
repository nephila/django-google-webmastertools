# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP ',
]

setup(
    author="Nephila s.a.s.",
    author_email='web@nephila.it',
    name='google_webmastertools',
    version='0.1.0',
    description='Django interface to Google Webmaster tools API',
#    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://www.nephila.it',
    license='see LICENCE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        "Django < 1.4",
        "gdata >= 2.0.17",
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
    ],
)
