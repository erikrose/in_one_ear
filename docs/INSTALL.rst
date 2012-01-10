Python Versions
===============

2.7 and 2.6 work. 2.5 might as well.


Install PostgreSQL
==================

After installing Postgres, initialize a database cluster, if it wasn't done
automatically. Here how to do it on a Mac if you used the MacPorts package::

    mkdir -p /opt/local/var/db/postgresql84/defaultdb
    chown postgres:postgres /opt/local/var/db/postgresql84/defaultdb
    su postgres -c '/opt/local/lib/postgresql84/bin/initdb -D /opt/local/var/db/postgresql84/defaultdb'
    su postgres -c '/opt/local/lib/postgresql84/bin/postgres -D /opt/local/var/db/postgresql84/defaultdb'


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
