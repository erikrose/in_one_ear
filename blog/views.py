from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


from blog.models import Article


def article_list(request):
    """List all the articles, newest first."""
    # TODO: Paginate or something.
    return render_to_response(
        'blog/article_list.html',
        {'articles': Article.objects.all().order_by('-created')})


def article(request, slug):
    """Show a particular article."""
    article = get_object_or_404(Article, slug=slug)
    return render_to_response(
        'blog/article.html',
        {'article': article})
