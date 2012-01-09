from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import (Model, DateTimeField, TextField, DateField,
                              ForeignKey)
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _lazy


REST_INSTRUCTIONS = _lazy(u'Use reStructuredText.')


class Article(Model):
    """A blog article"""
    # In Postgres, "text" is identical to "varchar" without length limits, and
    # specifying limits only decreases performance. it has no effect on how
    # it's stored. Not giving a max length here saves a pricy migration,
    # inevitably, we want to increase it.
    title = TextField(db_index=True, unique=True)  # Index for admin search.
    slug = TextField(db_index=True, unique=True)
    created = DateTimeField(auto_now_add=True, db_index=True)  # Index for sort
    body = TextField(blank=True,  # Can be blank. Why be obnoxious?
                     help_text=REST_INSTRUCTIONS)

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        """If a slug wasn't provided, make one up based on the title."""
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)


class Comment(Model):
    """A comment attached to a blog article"""
    creator = ForeignKey(User, null=True)
    article = ForeignKey(Article, related_name='comments')
    body = TextField(help_text=REST_INSTRUCTIONS)

    class Meta(object):
        ordering = ['id']

    def __unicode__(self):
        return unicode(self.body)
