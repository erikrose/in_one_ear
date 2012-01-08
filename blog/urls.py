from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'article_list', name='blog.article_list'),
    url(r'^(?P<slug>[^/]+)/', 'article', name='blog.article')
)