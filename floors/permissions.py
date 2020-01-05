from rest_framework import permissions

from floors.models import Floor


class LimitedFloorPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        floors = Floor.objects.filter(park=obj.park)

        print(obj.park.limit_floor, floors.count())

        if obj.park.limit_floor <= floors.count():
            return False

        return True
