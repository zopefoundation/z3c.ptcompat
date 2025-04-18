##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED 'AS IS' AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup
"""
import os

from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


TESTS_REQUIRE = [
    "zope.configuration",
    "zope.testing",
    "zope.testrunner >= 6.4"]

setup(
    name="z3c.ptcompat",
    version="5.1.dev0",
    description="Zope-compatible page template engine based on Chameleon.",
    long_description="\n\n".join(
        (".. contents::", read("README.rst"), read("CHANGES.rst"))
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone",
        "Framework :: Zope :: 3",
        "Framework :: Zope :: 5",
    ],
    keywords="zpt template zope",
    url="https://github.com/zopefoundation/z3c.ptcompat",
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'z3c.ptcompat/issues'),
        'Sources': 'https://github.com/zopefoundation/z3c.ptcompat',
    },
    author="Zope Foundation and Contributors",
    author_email="zope-dev@zope.dev",
    license="ZPL",
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.9',
    install_requires=[
        "setuptools",
        "z3c.pt >= 3.0.0a1",
        "zope.pagetemplate >= 3.6.2",
        "zope.traversing",
    ],
    extras_require={"test": TESTS_REQUIRE},
)
