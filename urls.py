from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # The requirements say to park the articles at the root, so we do that:
    url(r'', include('blog.urls'))
)
