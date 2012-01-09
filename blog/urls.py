from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'article_list', name='blog.article_list'),
    url(r'^(?P<slug>[^/]+)/$', 'article', name='blog.article'),
    url(r'^(?P<slug>[^/]+)/edit$', 'edit_article', name='blog.edit_article'),
    url(r'^(?P<slug>[^/]+)/delete$', 'delete_article', name='blog.delete_article'),
    url(r'^new$', 'new_article', name='blog.new_article')
)
