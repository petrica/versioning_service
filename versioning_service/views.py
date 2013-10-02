from django.views.generic.base import RedirectView

from django.core.urlresolvers import reverse


class ToAppList(RedirectView):

    def get_redirect_url(self):
        return reverse('list_apps')
    # pattern_name = 'list_apps'
