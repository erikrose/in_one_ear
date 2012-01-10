Python Versions
===============

2.7 and 2.6 work. 2.5 might as well.


Set Settings
============

In the ``settings`` folder, copy ``local.py-dist`` to ``local.py``, and edit
the latter with your DB credentials, ``STATIC_ROOT`` value, etc.

The FS division between local and stock settings is something we use at Mozilla
to avoid accidentally committing machine-specific things. It works pretty well.


Install Dependencies
====================

Use pip to install the dependencies listed in ``requirements.txt``::

  pip install -r in_one_ear/requirements.txt


Collect Static Assets
=====================

./manage.py collectstatic


Run The Tests
=============

To be sure everything's copasetic, run ``manage.py test``.
