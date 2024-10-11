from django.db.models import Count, OuterRef, Sum, F, Case, When, Value, FloatField, IntegerField
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework import serializers
from app.commons.db_functions import SubqueryCount
from app.models import RelationSell, Seller


class SellerSaleStatSerializer(serializers.ModelSerializer):
    number_sale_model = serializers.IntegerField()
    number_sale_option = serializers.IntegerField()
    concession = serializers.SerializerMethodField()
    percent_sales_total = serializers.IntegerField()
    percent_sales_concession = serializers.IntegerField()
    avg_option_per_car = serializers.FloatField()
    total_sales = serializers.IntegerField()

    def get_concession(self, seller: Seller):
        concession = getattr(seller, "concession")
        return concession.zip if concession else None

    class Meta:
        model = Seller
        fields = [
            "id",
            "first_name",
            "last_name",
            "concession",
            "number_sale_model",
            "number_sale_option",
            "percent_sales_total",
            "percent_sales_concession",
            "avg_option_per_car",
            "total_sales"
        ]


class SellerSaleStatViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    # permission_classes
    serializer_class = SellerSaleStatSerializer

    def get_queryset(self):
        user: Seller = self.request.user

        if not user or user.is_anonymous:
            raise PermissionDenied()

        return Seller.objects.prefetch_related(
            "relations_sells__options",
            "relations_sells__carmodel"
        ).select_related("concession").filter(concession__isnull=False).annotate(
            number_sale_all=SubqueryCount(RelationSell.objects.all()),
            number_sale_concession=SubqueryCount(RelationSell.objects.filter(seller__concession=OuterRef("concession")).values("id")),
            number_sale_model=SubqueryCount(RelationSell.objects.filter(seller_id=OuterRef("id"))),
            number_sale_option=Count("relations_sells__options"),
            total_sales_model=Sum("relations_sells__carmodel__price"),
            total_sales_option=Sum("relations_sells__options__price")
        ).annotate(
            percent_sales_total=Case(
                When(number_sale_all__gt=0, then=(F("number_sale_model") * 100) / F("number_sale_all")),
                default=Value(0),
                output_field=IntegerField()
            ),
            percent_sales_concession=Case(
                When(number_sale_concession__gt=0, then=(F("number_sale_model") * 100) / F("number_sale_concession")),
                default=Value(0),
                output_field=IntegerField()
            ),
            avg_option_per_car=Case(
                When(number_sale_model__gt=0, then=F("number_sale_option")),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            total_sales=F("total_sales_model") + F("total_sales_option")
        )
