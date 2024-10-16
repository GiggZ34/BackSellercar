from django.db.models import Sum, Value, F
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models.functions import Coalesce
from app.constantes import SellerRoles
from app.models import RelationSell, Seller
from app.serializers import RelationSellModelSerializer
from app.permissions import RelationSellPermission
from app.serializers.relation_sell_model import PostRelationSellModelSerializer
from rest_framework.response import Response
import math


class CustomPagination(PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        total_items = self.page.paginator.count
        total_pages = math.ceil(total_items / self.page_size)

        return Response({
            'count': total_items,
            'total_pages': total_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


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
    pagination_class = CustomPagination
    filterset_fields = ('customer_id', 'seller_id')

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
