from django.forms import ModelForm

from apps.models import VersionedApp


class VersionedAppForm(ModelForm):
    class Meta:
        model = VersionedApp
        fields = ['name']
