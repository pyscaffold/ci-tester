=========
ci-tester
=========


Internal dummy repository to test PyScaffold's several UI integrations (FOR TESTING PURPOSES ONLY)
It should be updated (forcefully if necessary) every time a change that impacts PyScaffold's CI
integrations is made (a PR on PyScaffold's main repository that changes CI is
expected to provide a companion PR to this repository).


.. pyscaffold-notes::

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

.. _pre-commit: http://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.0b3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
