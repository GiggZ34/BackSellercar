from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import app.models
from app.constantes import SellerRoles
from app.models import RelationSell, Seller
from app.serializers import RelationSellModelSerializer
from app.permissions import RelationSellPermission
from app.serializers.relation_sell_model import PostRelationSellModelSerializer


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

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RelationSellModelSerializer

        return PostRelationSellModelSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)