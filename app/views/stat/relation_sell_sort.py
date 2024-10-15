from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.exceptions import PermissionDenied

from app.models import Seller


class RelationSellSortView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    def get_queryset(self):
        user: Seller = self.request.user

        if not user or user.is_anonymous:
            raise PermissionDenied()

