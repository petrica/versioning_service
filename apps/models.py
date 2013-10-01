from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from tastypie.models import create_api_key


models.signals.post_save.connect(create_api_key, sender=User)


class VersionedApp(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'details_versioned_app',
            kwargs={'pk': self.id}
        )

    def branches(self):
        return self.branch_set.all()


class Branch(models.Model):
    related_app = models.ForeignKey(VersionedApp)
    name = models.CharField(max_length=255)

    def highest_version(self):
        version = self.branchversion_set.all().latest("version_number")
        if version:
            return version.version_number
        else:
            return 0


class BranchVersion(models.Model):
    related_branch = models.ForeignKey(Branch)
    version_number = models.IntegerField()
    commit_hash = models.CharField(max_length=40)
