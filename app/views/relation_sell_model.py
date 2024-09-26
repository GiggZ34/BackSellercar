from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import app.models
from app.constantes import SellerRoles
from app.models import RelationSell, Seller
from app.serializers import RelationSellModelSerializer
from app.permissions import RelationSellPermission


class RelationSellModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = RelationSellModelSerializer
    permission_classes = [RelationSellPermission]

    def get_queryset(self):
        user: Seller = self.request.user

        if user.is_anonymous:
            return RelationSell.objects.none()

        query_role_mapped = {
            SellerRoles.ELON: RelationSell.objects.all(),
            SellerRoles.OWNER: RelationSell.objects.select_related("seller").filter(seller__concession=user.concession),
            SellerRoles.STANDARD: RelationSell.objects.filter(seller=user)
        }

        return query_role_mapped[user.roles]
