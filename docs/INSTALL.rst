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
the latter with your DB credentials.
