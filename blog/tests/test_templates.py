from django.core.urlresolvers import reverse
from django.test import TestCase

from nose.tools import eq_

from blog.tests import article


class ArticlesTests(TestCase):
    """Tests for the article list"""

    def test_articles_show_up(self):
        """Assert (multiple) articles show up on the front page."""
        article(title='Improbable').save()
        article(title='Dwarves').save()

        response = self.client.get(reverse('blog.article_list'))
        self.assertContains(response, 'Improbable')
        self.assertContains(response, 'Dwarves')
