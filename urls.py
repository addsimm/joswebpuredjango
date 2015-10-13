
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'joswebpuredjango.views.home', name='home'),
    # url(r'^joswebpuredjango/', include('joswebpuredjango.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    # url('', include('social.apps.django_app.urls', namespace = 'social')),
    # url(r'login', 'joswebcloudsql.views.login', name = 'login'),
    # url(r'^$', 'joswebcloudsql.views.landing_page', name = 'landing_page')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
