from datetime import datetime

from django.db.models import Model, DateTimeField, TextField, DateField


class Article(Model):
    # In Postgres, "text" is identical to "varchar" without length limits, and
    # specifying limits only decreases performance. it has no effect on how
    # it's stored. Not giving a max length here saves a pricy migration,
    # inevitably, we want to increase it.
    title = TextField(db_index=True, unique=True)  # Index for admin search.
    slug = TextField(db_index=True, unique=True)
    created = DateTimeField(auto_now_add=True, db_index=True)  # Index for sort
    body = TextField()

    def __unicode__(self):
        return unicode(self.title)
