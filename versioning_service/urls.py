from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apps.views import ListApps

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'versioning_service.views.home', name='home'),
    # url(r'^versioning_service/', include('versioning_service.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^', include('apps.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', ListApps.as_view())
)
