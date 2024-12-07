coverage-p
=============

.. |pypi| image:: https://img.shields.io/pypi/v/coverage-p.svg
    :alt: PyPI
    :target: https://pypi.org/project/coverage-p/

.. |calver| image:: https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg
    :alt: calver: YY.MM.MICRO
    :target: https://calver.org/

.. |ci| image:: https://github.com/twm/coverage-p/actions/workflows/ci.yml/badge.svg
    :alt: CI
    :target: https://github.com/twm/coverage-p/actions/workflows/ci.yml


|pypi|
|calver|
|ci|

This package contains a ``.pth`` file that calls ``coverage.process_startup()``.

.. contents::

Usage
-----

Install it with Pip::

    $ pip install coverage-p

Then run your tests like::

    $ COVERAGE_PROCESS_START="$PWD/.coveragerc" coverage run -p -m unittest ...

Each Python processes your tests spawn will generate a ``.coverage`` file.
Merge these by running ``coverage combine``.

See the Coverage.py document `Measuring sub-processes <https://coverage.readthedocs.io/en/latest/subprocess.html>`__ for more information.

.. note::

   ``coverage.process_startup()`` is a no-op unless the ``COVERAGE_PROCESS_START`` environment variable is set.
   The ``coverage run`` command does *not* set this variable!

Why not ``coverage_pth``?
~~~~~~~~~~~~~~~~~~~~~~~~~

The `coverage_pth package <https://pypi.org/project/coverage_pth/>`__ attempts to do the same thing,
but the wheels it provides only work on Python 3.6.
It also `appears unmaintained <https://github.com/dougn/coverage_pth/commits/master/>`__.

Compatiblity Policy
-------------------

Any version of CPython `supported upstream <https://devguide.python.org/versions/>`_ and by Coverage.py is considered supported and should be tested in CI.
Additionally, CI covers supported 3.x releases of `PyPy <https://pypy.org/>`_, subject to availability in GitHub Actions.

coverage-p is tested against the current version of Coverage.py.
The API coverage-p invokes has been stable for many years, so compatibility issues are not expected.

Changelog
---------

v24.7.0 (2024-07-06)
~~~~~~~~~~~~~~~~~~~~

- Initial release


Contributing
------------

File issues and PRs `on GitHub <https://github.com/twm/coverage-p/issues>`__.
See `CONTRIBUTING.rst <./CONTRIBUTING.rst>`__ for more.
Please follow the `Twisted code of conduct <https://github.com/twisted/.github/blob/trunk/code_of_conduct.md>`__.


License
-------

coverage-p is made available under the `MIT license <./LICENSE>`__.
