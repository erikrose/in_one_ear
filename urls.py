from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Use the stock auth stuff:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='in_one_ear.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/was_logged_out.html'}, name='in_one_ear.logout'),  # Can't seem to override default logged_out.html template.

    # The requirements say to park the articles at the root, so we do that:
    url(r'', include('in_one_ear.blog.urls'))
)
