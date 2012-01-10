from django.test import TestCase

from nose.tools import eq_

from in_one_ear.blog.models import Article
from in_one_ear.blog.tests import article


class ArticleTests(TestCase):
    """Tests for the Article model"""

    def test_unicode(self):
        """Make sure the ``__unicode__`` method returns the title."""
        result = unicode(article(title='Hi There'))
        eq_(type(result), type(u''))
        eq_(result, u'Hi There')

    def test_slug_making(self):
        """Make sure the model makes up a good slug when one isn't provided."""
        a = Article(title='Hello Dolly')
        a.save()

        a_saved = Article.objects.get(title='Hello Dolly')
        eq_(a_saved.slug, 'hello-dolly')
