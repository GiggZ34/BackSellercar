from django.db.models import Count, OuterRef, Sum, F, Case, When, Value, FloatField
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.exceptions import PermissionDenied

from app.commons.db_functions import SubquerySum
from app.models import RelationSell, Seller, Concession


class ConcessionStatSerializer(serializers.ModelSerializer):
    total_selled_car = serializers.IntegerField()
    total_selled = serializers.IntegerField()
    number_sale_all_price = serializers.IntegerField()
    total_selled_model_price = serializers.IntegerField()
    total_selled_options_price = serializers.IntegerField()
    percent_of_total_selled = serializers.FloatField()

    class Meta:
        model = Concession
        fields = [
            "id",
            "total_selled_car",
            "number_sale_all_price",
            "total_selled_model_price",
            "total_selled_options_price",
            "total_selled",
            "percent_of_total_selled",
        ]


class ConcessionStatViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    serializer_class = ConcessionStatSerializer

    def get_queryset(self):
        user: Seller = self.request.user

        if not user or user.is_anonymous:
            raise PermissionDenied()

        return Concession.objects.annotate(
            total_selled_car=Count("sellers__relations_sells"),
            total_selled_model_price=Sum("sellers__relations_sells__carmodel__price"),
            total_selled_options_price=SubquerySum(
                RelationSell.objects.filter(seller__concession_id=OuterRef("id")).values(value=F("options__price"))),
            number_sale_all_price=SubquerySum(RelationSell.objects.values(value=F("carmodel__price"))) + SubquerySum(
                RelationSell.objects.values(value=F("options__price"))),
        ).annotate(
            total_selled=F("total_selled_model_price") + F("total_selled_options_price"),
            percent_of_total_selled=Case(
                When(number_sale_all_price__gt=0,
                     then=(F("total_selled_model_price") + F("total_selled_options_price")) * 100 / F(
                         "number_sale_all_price")),
                default=Value(0.0),
                output_field=FloatField()
            )
        )
