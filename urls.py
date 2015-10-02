from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joswebpuredjango.views.home', name='home'),
    # url(r'^joswebpuredjango/', include('joswebpuredjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'login', 'joswebcloudsql.views.login', name = 'login'),
    url(r'^$', 'joswebcloudsql.views.landing_page', name = 'landing_page')
)
