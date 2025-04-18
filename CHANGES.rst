Changelog
=========

5.1 (unreleased)
----------------

- Nothing changed yet.


5.0 (2025-04-14)
----------------

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


4.1 (2025-04-09)
----------------

- Add support for Python 3.13.

- Drop support for Python 3.8.


4.0 (2024-06-07)
----------------

- Drop support for Python 3.7.

- Add support for Python 3.12.


3.0 (2024-01-09)
----------------

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


2.3.0 (2021-12-16)
------------------

- Add support for Python 3.8, 3.9, and 3.10.

- Drop support for Python 3.4.


2.2.0 (2019-01-27)
------------------

- Add support for Python 3.7.

- Drop support for running the tests using `python setup.py test`


2.1.0 (2017-10-17)
------------------

- Fix rendering with Chameleon 3.0 and above. See `issue 2
  <https://github.com/zopefoundation/z3c.ptcompat/issues/2>`_.
- Add support for Python 3.6.
- Drop support for Python 3.3.


2.0 (2016-09-02)
----------------

- Added support for Python 3.4, 3.5, PyPy and PyPy3.

- Dropped support for Python 2.6.


2.0.0a1 (2013-02-25)
--------------------

- Added support for Python 3.3.

- Ensured that ``chameleon.tal.ReapeatDict`` can be adapted. (Needs to be
  fixed in Chameleon.)

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


1.0.1 (2012-02-15)
------------------

- Move ``zope.testing`` to test dependencies, add undeclared dependencies.


1.0 (2011-10-10)
----------------

- Update implementation to use component-based template engine
  configuration, plugging directly into the Zope Toolkit framework.

  The package no longer provides template classes, or ZCML directives;
  you should import directly from the ZTK codebase.

  Also, note that the ``PREFER_Z3C_PT`` environment option has been
  rendered obsolete; instead, this is now managed via component
  configuration.

- Upgrade to Chameleon 2.x.

0.5.7 (2010-11-25)
------------------

- Added not yet declared test dependency on ``zope.testing``.

- Fixed test tear down so tests can be run multiple times.


0.5.6 (2010-04-19)
------------------

- Remove broken templates from registry during engine migration. In
  some testing situation, stale templates would be tracked in the
  regsitry.

- Existing template instances are now migrated to the right engine
  when using the ``enable`` and ``disable`` methods. [malthe]

0.5.5 (2009-07-24)
------------------

- Make tests pass in a binary release by not relying on the pacakge structure.

0.5.4 (2009-07-23)
------------------

- Added a test requirement explicitely.

0.5.3 (2009-05-28)
------------------

- Added support for browser:addform, browser:editform, browser:form,
  and browser:schemadisplay directives.

0.5.2 (2009-03-09)
------------------

- Fixing brown-bag release 0.5.1.

0.5.1 (2009-03-09)
------------------

- Added missing ``lxml`` test dependency.

- Fixed tests to work with current version of z3c.pt.

- Fixed autor e-mail address.

- Added doctests and change log to long description to show up at pypi
  homepage.

- Reformatted release dates in change log to use iso dates.

0.5 (2009-02-16)
----------------

- Added module which patches ``zope.app.pagetemplate`` such that
  template classes depend on ``z3c.pt`` for rendering (import
  optional). [malthe]

0.4 (2009-02-10)
----------------

- Rename project to z3c.ptcompat to deal with setuptools issues (as discussed
  on zope-dev http://mail.zope.org/pipermail/zope-dev/2008-December/033820.html)

- Added optional option ``doctest`` for output checker to allow usage
  with alternative implementations, e.g. the Zope doctest
  module. [malthe]

- Added tests for meta-directives and fixed some minor errors. [malthe]

- Added update-tool to walk a source tree and automatically rewrite
  template import statements in each file. [malthe]

- Added meta-directives for browser pages and viewlets. These build
  upon the original implementations, but make sure that the Chameleon
  template engine is used. [malthe]

- Added ``PageTemplateFile``. [malthe]

0.3 (2008-10-02)
----------------

- Various changes.

0.2 (2008-09-13)
----------------

- Various changes.

0.1 (2008-09-09)
----------------

- Initial release.
