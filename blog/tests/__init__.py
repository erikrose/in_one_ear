# -*- coding: utf-8 -*-
"""Support machinery for blog-app tests"""
from datetime import datetime
from functools import wraps
import random
from string import letters

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from blog.models import Article


def with_save(func):
    """Decorate a model maker to add a `save` kwarg.

    If save=True, the model maker will save the object before returning it.

    """
    @wraps(func)
    def saving_func(*args, **kwargs):
        save = kwargs.pop('save', False)
        ret = func(*args, **kwargs)
        if save:
            ret.save()
        return ret

    return saving_func


@with_save
def article(**kwargs):
    """Make and return a minimal saveable Article for use in tests.

    This is a "model maker", a pattern that serves the same end as Django's
    fixtures but better. In anything but the smallest projects, fixtures tend
    to hurt performance (since they're by default reloaded before each test),
    comprehensibility (since fixture data is not lexically proximal to the test
    code that uses it) and maintainability (since they promote coupling between
    tests). Model makers fix all of these.

    The performance concerns can be ameliorated by doing crazy things like I
    describe in
    http://groups.google.com/group/django-developers/browse_thread/thread/
    65a36a8a5433144c (included in the current trunk of django-nose), but I
    didn't have time to throw together a release of that this weekend, and it
    doesn't solve the other two problems. I'll be giving a more comprehensive
    treatment in an upcoming PyCon talk:
    http://groups.google.com/group/django-developers/browse_thread/thread/
    65a36a8a5433144c.

    """
    options = kwargs
    if 'title' not in options:
        # I often throw arbitrary Unicode into my test data, as it helps
        # uncover Unicode-unclean code:
        options['title'] = u'☃' + str(datetime.now())  # pretty good rez
    if 'slug' not in options:
        options['slug'] = slugify(options['title'])

    return Article(**options)


@with_save
def user(**kwargs):
    """Return a user with all necessary defaults filled in.

    Default password is 'testpass' unless you say otherwise in a kwarg.

    """
    defaults = {}
    if 'username' not in kwargs:
        defaults['username'] = ''.join(random.choice(letters)
                                       for x in xrange(15))
    defaults.update(kwargs)
    user = User(**defaults)
    user.set_password(kwargs.get('password', 'testpass'))
    return user
