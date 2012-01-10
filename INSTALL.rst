I hope these instructions are exactly vague enough for someone who's done this
before to do it again fast.


Make A Virtualenv
=================

Make a virtualenv, then drop (or link) ``in_one_ear`` into ``site-packages``.
(Sorry, no ``setup.py`` yet.) Python 2.7 and 2.6 work. 2.5 might as well.

Use pip to install the dependencies listed in ``requirements.txt``::

  pip install -r in_one_ear/requirements.txt

You might get away with newer versions, but I've pinned ones I know to work. In
particular, psycopg2<=2.4.1 is required. They overhauled some transaction stuff
after that that breaks Django 1.3.x. Django 1.4 will put up with it.


Set Up PostgreSQL
=================

I've included a conservative ``pg_hba.conf`` in the ``config`` directory.
You'll probably want to make your own changes. One thing to note is my
"sameuser" line. It's not the tightest thing in the world, security-wise, but
it sure cuts down on configuration needed for the common case of app users
which are called the same thing as their database. If you call both your In One
Ear user and your DB ``in_one_ear``, it will serve you well.

Make a database.


Set Settings
============

In the ``settings`` folder, copy ``local.py-dist`` to ``local.py``, and edit
the latter with your DB credentials, ``STATIC_ROOT`` value, etc.

The FS division between local and stock settings is something we use at Mozilla
to avoid accidentally committing machine-specific things. It works pretty well,
so I kept it.


Run syncdb
==========

Enough said.


Run The Tests
=============

To be sure everything's copasetic, run ``manage.py test``.


Collect Static Assets
=====================

./manage.py collectstatic


Set Up Apache
=============

A working vhost is in ``config/in_one_ear.conf``, but you'll need to replace my
paths with yours.


Create Users
============

Once you've made your first superuser either by following prompts or by
twiddling the DB, you can use the standard admin UI at ``/admin`` for the rest.
