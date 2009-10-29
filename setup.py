#!/usr/bin/python

import sys, os

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.0'

# For the love of god, use Pip to install this.

# Distutils version
METADATA = dict(
	name = "pythentic_jobs",
	version = __version__,
	py_modules = ['pythentic_jobs'],
	author='Ryan McGrath',
	author_email='ryan@venodesigns.net',
	description='A small (pure Python) wrapper around the Authentic Jobs (http://www.authenticjobs.com) API.',
	long_description= open("README.markdown").read(),
	license='MIT License',
	url='http://github.com/ryanmcgrath/pythentic_jobs/tree/master',
	keywords='jobs careers api',
)

# Setuptools version
SETUPTOOLS_METADATA = dict(
	install_requires = ['setuptools', 'simplejson'],
	include_package_data = True,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet',
	]
)

def Main():
	try:
		import setuptools
		METADATA.update(SETUPTOOLS_METADATA)
		setuptools.setup(**METADATA)
	except ImportError:
		import distutils.core
		distutils.core.setup(**METADATA)

if __name__ == '__main__':
  Main()
