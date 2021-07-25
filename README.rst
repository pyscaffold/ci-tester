.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://readthedocs.org/projects/ci-tester/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://ci-tester.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/pypi/v/ci-tester.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/ci-tester/
    .. image:: https://img.shields.io/conda/vn/conda-forge/ci-tester.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/ci-tester
    .. image:: https://pepy.tech/badge/ci-tester/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/ci-tester

.. image:: https://api.cirrus-ci.com/github/pyscaffold/ci-tester.svg?branch=main
    :alt: Built Status
    :target: https://cirrus-ci.com/github/pyscaffold/ci-tester
.. image:: https://img.shields.io/coveralls/github/pyscaffold/ci-tester/main.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/pyscaffold/ci-tester
.. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
    :alt: Twitter
    :target: https://twitter.com/ci-tester
.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=========
ci-tester
=========

    Internal dummy repository to test PyScaffold's several CI integrations **(FOR TESTING PURPOSES ONLY)**.

It should be updated (forcefully if necessary) every time a change that impacts PyScaffold's CI
integrations is made (a PR on PyScaffold's main repository that changes CI is
expected to provide a companion PR to this repository).

After a forced update with ``putup --no-config -U -f .``, don't forget to
reconcile the changes (specially in the ``README.rst`` and ``.cirrus.yml``
files) using ``git difftool``.


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd ci-tester
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.0.2.post1.dev60+g1585605. For details and usage
information on PyScaffold see https://pyscaffold.org/.
