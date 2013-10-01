from django.conf.urls import patterns, url, include

from apps.views import CreateVersionedApp, DetailVersionedApp, ListApps
from apps.api import v1_api

urlpatterns = patterns(
    'apps',

    url(
        r'^apps/$',
        ListApps.as_view(),
        name="list_apps"
    ),

    url(
        r'^apps/create/$',
        CreateVersionedApp.as_view(),
        name="create_versioned_app"
    ),

    url(
        r'^apps/(?P<pk>\d)/$',
        DetailVersionedApp.as_view(),
        name="details_versioned_app"
    ),
    url(
        r'^api/',
        include(v1_api.urls)
    ),

)
