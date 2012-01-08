from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import (require_GET, require_POST,
                                          require_http_methods)

from blog.forms import ArticleForm
from blog.models import Article


@require_GET
def article_list(request):
    """List all the articles, newest first."""
    # TODO: Paginate or something.
    return render_to_response(
        'blog/article_list.html',
        {'articles': Article.objects.all().order_by('-created')})


@require_GET
def article(request, slug):
    """Show a particular article."""
    article = get_object_or_404(Article, slug=slug)
    return render_to_response('blog/article.html', {'article': article})


@require_http_methods(['GET', 'POST'])
def edit_article(request, slug):
    """Edit an existing article.

    Only staff can edit, but they can edit anything: theirs or not. We're all
    adults here.

    """
    if not request.user.is_staff:
        return HttpResponseForbidden()

    article = get_object_or_404(Article, slug=slug)

    if request.method == 'GET':
        form = ArticleForm(instance=article)
        return render_to_response('blog/edit_article.html',
                                  {'form': form,
                                   'article': article},
                                  context_instance=RequestContext(request))
    else:  # POST
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # TODO: Handle uniqueness violations gracefully.
            return HttpResponseRedirect(reverse('blog.article', args=[article.slug]))
        else:
            # At the moment, there is no invalidity possible.
            raise NotImplementedError
