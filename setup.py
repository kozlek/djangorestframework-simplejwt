#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from io import open
import os
import re
import shutil
import sys

from setuptools import setup, find_packages


init_py = open(os.path.join('rest_framework_simplejwt', '__init__.py')).read()
version = re.search(r'''^__version__ = ['"]([^'"]+)['"]$''', init_py).group(1)


if sys.argv[-1] == 'publish':
    if os.system('pip freeze | grep twine'):
        print('twine not installed.\nUse `pip install twine`.\nExiting.')
        sys.exit()
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    print('You probably want to also tag the version now:')
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print('  git push --tags')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('djangorestframework.egg-info')
    sys.exit()


setup(
    name='djangorestframework_simplejwt',
    version=version,
    url='https://github.com/davesque/django-rest-framework-simplejwt',
    license='MIT',
    description='A bare-bones JSON Web Token authentication plugin for Django REST Framework',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='David Sanders',
    author_email='davesque@gmail.com',
    packages=find_packages(exclude=['tests', 'licenses', 'requirements']),
    install_requires=['django', 'djangorestframework', 'python-jose'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)