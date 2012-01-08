from datetime import datetime

from django.db.models import Model, DateTimeField, TextField, DateField


class Article(Model):
    # In Postgres, "text" is identical to "varchar" without length limits, and
    # specifying limits only decreases performance. it has no effect on how
    # it's stored. Not giving a max length here saves a pricy migration,
    # inevitably, we want to increase it.
    title = TextField()  # TODO: index?
    slug = TextField(db_index=True)
    created = DateTimeField(auto_now_add=True, db_index=True)  # index for sort
    body = TextField()
