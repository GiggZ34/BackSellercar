from rest_framework.permissions import BasePermission


class RelationSellPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj) -> bool:
        return super().has_object_permission(request, view, obj)
