from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import (require_GET, require_POST,
                                          require_http_methods)

from blog.forms import ArticleForm, CommentForm
from blog.models import Article


@require_GET
def article_list(request):
    """List all the articles, newest first."""
    # TODO: Paginate or something.
    return _render_contextually(
        request,
        'blog/article_list.html',
        {'articles': Article.objects.all().order_by('-created')})


@require_GET
def article(request, slug):
    """Show a particular article."""
    article = get_object_or_404(Article, slug=slug)
    return _render_contextually(request,
                                'blog/article.html',
                                {'article': article,
                                 'comment_form': CommentForm()})


@require_http_methods(['GET', 'POST'])  # Don't want to think about TRACE, etc.
def new_article(request):
    """Show the new-article form or actually create a new article."""
    if not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Handle uniqueness violations gracefully.
            return HttpResponseRedirect(reverse('blog.article',
                                        args=[form.instance.slug]))
    else:  # GET
        form = ArticleForm()

    # Form is invalid, or it's a GET.
    return _render_contextually(request,
                                'blog/new_article.html',
                                {'form': form})


@require_http_methods(['GET', 'POST'])
def edit_article(request, slug):
    """Edit an existing article.

    Only staff can edit, but they can edit anything: theirs or not. We're all
    adults here.

    """
    if not request.user.is_staff:
        return HttpResponseForbidden()

    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # TODO: Handle uniqueness violations gracefully.
            return HttpResponseRedirect(reverse('blog.article',
                                        args=[article.slug]))
    else:  # GET
        form = ArticleForm(instance=article)

    # Form is invalid, or it's a GET.
    return _render_contextually(request,
                                'blog/edit_article.html',
                                {'form': form, 'article': article})


@require_POST
def delete_article(request, slug):
    """Delete an existing article."""
    if not request.user.is_staff:
        return HttpResponseForbidden()

    Article.objects.get(slug=slug).delete()
    # If it wasn't there, no big deal. The end state is the same.
    return HttpResponseRedirect(reverse('blog.article_list'))


@require_POST
def new_comment(request, slug):
    """Attach a new comment to the given article."""
    article = get_object_or_404(Article, slug=slug)
    # TODO: Quit fetching anything but ID from the article.
    form = CommentForm(request.POST)

    # Comment form is always valid.
    comment = form.save(commit=False)
    if not request.user.is_anonymous():
        comment.creator = request.user
    comment.article = article
    comment.save()
    #form.save_m2m()  # Does nothing, of course
    return HttpResponseRedirect(reverse('blog.article',
                                args=[slug]))  # TODO: add anchor


def _render_contextually(request, *args, **kwargs):
    """Do like render_to_response but implicitly include a RequestContext"""
    return render_to_response(*args, context_instance=RequestContext(request))
