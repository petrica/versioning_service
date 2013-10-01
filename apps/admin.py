from django.contrib import admin

from apps.models import VersionedApp, Branch, BranchVersion

admin.site.register(VersionedApp)
admin.site.register(Branch)
admin.site.register(BranchVersion)
