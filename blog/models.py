from datetime import datetime
from docutils.core import publish_parts
from docutils.writers import html4css1

from django.db.models import Model, DateTimeField, TextField, DateField
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _lazy


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
                     help_text=_lazy(u'Use reStructuredText.'))

    def __unicode__(self):
        return unicode(self.title)

    @property
    def body_html(self):
        """Return the HTML-rendered body.

        In a real system, we'd probably cache the rendered HTML.

        """
        # Keep authors from spilling the contents of local files into the post
        # or abusing raw HTML:
        secure_settings = {'file_insertion_enabled': 0,
                           'raw_enabled': 0,
                           'initial_header_level': 2,  # TODO: Doesn't work
                           '_disable_config': 1}
        return publish_parts(self.body,
                             writer=html4css1.Writer(),
                             settings_overrides=secure_settings)['html_body']

    def save(self, *args, **kwargs):
        """If a slug wasn't provided, make one up based on the title."""
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
