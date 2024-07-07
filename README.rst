coverage-proc
=============

.. |ci| image:: https://github.com/twm/coverage-proc/actions/workflows/ci.yml/badge.svg
    :alt: CI
    :target: https://github.com/twm/coverage-proc/actions/workflows/ci.yml

.. |pypi| image:: https://img.shields.io/pypi/v/coverage-proc.svg
    :alt: PyPI
    :target: https://pypi.org/project/coverage-proc/

.. |calver| image:: https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg
    :alt: calver: YY.MM.MICRO
    :target: https://calver.org/


|pypi|
|calver|
|ci|

This package contains a ``.pth`` file that calls ``coverage.process_startup()``.

.. contents::

Usage
-----

Install it with Pip::

    $ pip install coverage-proc

Then run your tests like::

    $ coverage run -p -m unittest ...

See the Coverage.py document `Measuring sub-processes <https://coverage.readthedocs.io/en/latest/subprocess.html>`__ for more information.


Why not ``coverage_pth``?
~~~~~~~~~~~~~~~~~~~~~~~~~

The `coverage_pth package <https://pypi.org/project/coverage_pth/>`__ attempts to do the same thing,
but the wheels it provides only work on Python 3.6.
It also `appears unmaintained <https://github.com/dougn/coverage_pth/commits/master/>`__.


Changelog
---------

v24.7.0 (2024-07-06)
~~~~~~~~~~~~~~~~~~~~

- Initial release


Contributing
------------

File issues and PRs `on GitHub <https://github.com/twm/coverage-proc/issues>`__.
See `CONTRIBUTING.rst <./CONTRIBUTING.rst>`__ for more.
Please follow the `Twisted code of conduct <https://github.com/twisted/.github/blob/trunk/code_of_conduct.md>`__.


License
-------

coverage-proc is made available under the `MIT license <./LICENSE>`__.
