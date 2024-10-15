from django.db.models import Sum, Value, F
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models.functions import Coalesce
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

        queryset = (
            query_role_mapped[user.roles]
            .annotate(total_price=F("carmodel__price") + Coalesce(Sum("options__price"), Value(0)))
            .annotate(total_options_price=Coalesce(Sum("options__price"), Value(0)))
        )

        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(*ordering.split(','))

        return queryset

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RelationSellModelSerializer

        return PostRelationSellModelSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
