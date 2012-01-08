from django.test import TestCase

from nose.tools import eq_

from blog.tests import article


class ArticleTests(TestCase):
    """Tests for the Article model"""

    def test_unicode(self):
        """Make sure the ``__unicode__`` method returns the title."""
        result = unicode(article(title='Hi There'))
        eq_(type(result), type(u''))
        eq_(result, u'Hi There')

    def test_body_html(self):
        """Make sure the body renders its restructured text."""
        a = article(body='*improbable*')
        assert '<em>improbable</em>' in a.body_html
