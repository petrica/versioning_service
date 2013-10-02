# Create your views here.
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.sites.models import Site

from apps.models import VersionedApp
from apps.forms import VersionedAppForm


class ListApps(ListView):
    model = VersionedApp

    def get_queryset(self):
        return super(ListApps, self).get_queryset().filter(
            owner=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super(ListApps, self).get_context_data(**kwargs)
        # print "context", context
        # print dir(self.request.user.api_key)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListApps, self).dispatch(*args, **kwargs)


class CreateVersionedApp(CreateView):
    model = VersionedApp
    form_class = VersionedAppForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateVersionedApp, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateVersionedApp, self).dispatch(*args, **kwargs)


class DetailVersionedApp(DetailView):
    model = VersionedApp

    def get_context_data(self, **kwargs):
        context = super(DetailVersionedApp, self).get_context_data(**kwargs)
        context['domain'] = Site.objects.get_current().domain
        return context

    def get_queryobject(self):
        return super(DetailVersionedApp, super).get_queryobject().filter(
            owner=self.request.user
        )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailVersionedApp, self).dispatch(*args, **kwargs)
