from rest_framework.permissions import BasePermission

from app.constantes import SellerRoles


class SellerPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        if view.action == 'update' or view.action == 'partial_update':
            return request.user.roles != SellerRoles.STANDARD
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj) -> bool:
        if view.action == 'update' or view.action == 'partial_update':
            return request.user.roles == SellerRoles.ELON \
                or (request.user.roles == SellerRoles.OWNER and request.user.concession == obj.concession)
        return super().has_object_permission(request, view, obj)
