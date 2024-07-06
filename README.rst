coverage.pth
============

|ci|
|pypi|

This package contains a ``.pth`` file that calls ``coverage.process_startup()``.

Usage
-----

Install it with Pip::

    pip install coverage.pth

Then run your tests like::

    coverage run -p -m unittest ...

See the Coverage.py document `Measuring sub-processes <https://coverage.readthedocs.io/en/latest/subprocess.html>`__ for more information.


Why not ``coverage_pth``?
-------------------------

The `coverage_pth package <https://pypi.org/project/coverage_pth/>`__ attempts to do the same thing,
but the wheels it provides only work on Python 3.6.
It also `appears unmaintained <https://github.com/dougn/coverage_pth/commits/master/>`__.

.. |gha| image:: https://github.com/twm/coverage.pth/actions/workflows/ci.yaml/badge.svg
.. _gha: https://github.com/twm/coverage.pthincremental/actions/workflows/ci.yaml

.. |pypi| image:: http://img.shields.io/pypi/v/coverage.pth.svg
.. _pypi: https://pypi.python.org/pypi/coverage.pth
