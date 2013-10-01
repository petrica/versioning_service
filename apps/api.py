from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import fields
from tastypie.constants import ALL
from tastypie.authentication import (
    BasicAuthentication,
    ApiKeyAuthentication,
    MultiAuthentication
)

from tastypie.authorization import DjangoAuthorization

from apps.models import VersionedApp, Branch, BranchVersion


class VersionedAppResource(ModelResource):
    class Meta:
        queryset = VersionedApp.objects.all()
        resource_name = 'versioned_app'
        filtering = {
            'name': ALL
        }
        authentication = MultiAuthentication(
            BasicAuthentication(),
            ApiKeyAuthentication()
        )
        authorization = DjangoAuthorization()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(owner=request.user)


class BranchResource(ModelResource):
    class Meta:
        queryset = Branch.objects.all()
        resource_name = 'branch'
        authentication = MultiAuthentication(
            BasicAuthentication(),
            ApiKeyAuthentication()
        )
        authorization = DjangoAuthorization()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(related_app__owner=request.user)


class BranchVersionResource(ModelResource):

    related_branch = fields.ToOneField(BranchResource, 'related_branch')

    class Meta:
        queryset = BranchVersion.objects.all()
        resource_name = 'branch_version'
        filtering = {
            'commit_hash': ALL,
            'related_branch': ALL,
        }

        authentication = MultiAuthentication(
            BasicAuthentication(),
            ApiKeyAuthentication()
        )

        authorization = DjangoAuthorization()

    def obj_get_list(self, bundle, **kwargs):

        objects = super(BranchVersionResource, self).obj_get_list(
            bundle,
            **kwargs
        )

        app = bundle.request.GET.get(
            'for_app',
            None
        )

        if app:
            objects = objects.filter(related_branch__related_app=app)

        branch_name = bundle.request.GET.get(
            'for_branch__name',
            None
        )

        if branch_name:
            objects = objects.filter(related_branch__name=branch_name)

        commit_hash = bundle.request.GET.get(
            'commit_hash',
            None
        )

        print app, branch_name, commit_hash

        if app and branch_name and commit_hash:
            queried_app = VersionedApp.objects.filter(
                owner=bundle.request.user,
                id=app
            )

            print "eh,,,", queried_app
            if queried_app.count() == 1:
                print "count", objects.count()
                if objects.count() == 0:
                    branch, new_branch = Branch.objects.get_or_create(
                        related_app=queried_app[0],
                        name=branch_name
                    )

                    print branch, new_branch

                    if new_branch is True:
                        # BranchResource
                        # branch = branch.create(
                        #     related_app=queried_app[0],
                        # )

                        bv = BranchVersion(
                            related_branch=branch,
                            version_number=1,
                            commit_hash=commit_hash
                        )

                        bv.save()
                    else:
                        versions = BranchVersion.objects.filter(
                            related_branch=branch,
                            # commit_hash=commit_hash
                        )

                        exact_hash_versions = versions.filter(
                            commit_hash=commit_hash
                        )

                        if exact_hash_versions.count() == 0:
                            if versions.count():
                                latest = versions.latest('version_number')
                                latest = latest.version_number
                            else:
                                latest = 0

                            bv = BranchVersion(
                                related_branch=branch,
                                version_number=latest+1,
                                commit_hash=commit_hash
                            )

                            bv.save()
                print locals()

        # print(
        #     objects,
        #     app,
        #     branch_name,
        #     bundle.request.GET.get('related_branch__related_app', None)
        # )

        return objects

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(
            related_branch__related_app__owner=request.user
        )

v1_api = Api(api_name='v1')
v1_api.register(VersionedAppResource())
v1_api.register(BranchResource())
v1_api.register(BranchVersionResource())
