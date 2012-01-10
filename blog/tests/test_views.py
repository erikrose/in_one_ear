"""Tests for views that are independent of what template they render"""

from django.core.urlresolvers import reverse
from django.test import TestCase

from nose.tools import eq_

from in_one_ear.blog.models import Article
from in_one_ear.blog.tests import article, user


class ViewTestCase(TestCase):
    """Test case base class with some handy convenience methods"""

    def _log_in_as_staff(self):
        u = user(is_staff=True, save=True)
        self.client.login(username=u.username, password='testpass')


class EditArticleTests(ViewTestCase):
    """Tests for the edit_article view"""

    @staticmethod
    def _edit_view(slug):
        return reverse('blog.edit_article', kwargs={'slug': slug})

    def test_staff_required(self):
        """Make sure non-staff users can't edit articles."""
        a = article(save=True)
        edit_view = self._edit_view(a.slug)

        # Can't see the edit screen; redirects to login:
        response = self.client.get(edit_view)
        eq_(response.status_code, 302)

        # And can't actually save:
        response = self.client.post(edit_view)
        eq_(response.status_code, 302)

    def test_edit(self):
        """Make sure staff can edit articles."""
        a = article(save=True)
        edit_view = self._edit_view(a.slug)

        # Make sure editing actually changes the instance:
        self._log_in_as_staff()
        self.client.post(edit_view, {'title': 'new title',
                                     'body': 'new body'})

        changed_article = Article.objects.get(pk=a.pk)
        eq_(changed_article.title, 'new title')
        eq_(changed_article.body, 'new body')

    def test_blank_title(self):
        """Assert posting a blank title shows an error."""
        a = article(save=True)
        edit_view = self._edit_view(a.slug)

        self._log_in_as_staff()
        response = self.client.post(edit_view, {'title': '',
                                                'body': 'new body'})
        self.assertContains(response, 'This field is required.')


class DeleteArticleTests(ViewTestCase):
    """Tests for the delete_article view"""

    def test_delete(self):
        """Make sure staff can delete articles."""
        a = article(save=True)

        # Make sure editing actually changes the instance:
        self._log_in_as_staff()
        response = self.client.post(reverse('blog.delete_article',
                                            args=[a.slug]),
                                    follow=True)
        eq_(response.status_code, 200)
        assert not Article.objects.all().exists()


class NewArticleTests(ViewTestCase):
    """Tests for making new articles"""

    def test_happy_path(self):
        """Assert new articles get made if everybody does everything right."""
        self._log_in_as_staff()
        response = self.client.post(reverse('blog.new_article'),
                                    {'title': 'improbable', 'body': 'dwarf'},
                                    follow=True)
        assert Article.objects.filter(title='improbable',
                                      body='dwarf').exists()
        self.assertContains(response, 'improbable')


# TODO: Write tests for commenting.
