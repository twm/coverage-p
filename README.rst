coveragepth
===========

|pypi|
|calver|
|ci|

This package contains a ``.pth`` file that calls ``coverage.process_startup()``.

Usage
-----

Install it with Pip::

    pip install coveragepth

Then run your tests like::

    coverage run -p -m unittest ...

See the Coverage.py document `Measuring sub-processes <https://coverage.readthedocs.io/en/latest/subprocess.html>`__ for more information.


Why not ``coverage_pth``?
-------------------------

The `coverage_pth package <https://pypi.org/project/coverage_pth/>`__ attempts to do the same thing,
but the wheels it provides only work on Python 3.6.
It also `appears unmaintained <https://github.com/dougn/coverage_pth/commits/master/>`__.

.. |ci| image:: https://github.com/twm/coveragepth/actions/workflows/ci.yml/badge.svg
    :alt: CI
    :target: https://github.com/twm/coveragepth/actions/workflows/ci.yml

.. |pypi| image:: https://img.shields.io/pypi/v/coveragepth.svg
    :alt: PyPI
    :target: https://pypi.org/project/coveragepth/

.. |calver| image:: https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg
    :alt: calver: YY.MM.MICRO
    :target: https://calver.org/

