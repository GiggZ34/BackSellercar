from django.db.models import Count, F, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.commons.db_functions import SubquerySum
from app.models import RelationSell, Concession, Seller
from rest_framework.exceptions import PermissionDenied


class GeneralStatView(APIView):

    def get(self, request, *args, **kwargs):

        user: Seller = self.request.user

        if not user or user.is_anonymous:
            raise PermissionDenied()

        # Request
        top_selled_car = (
            RelationSell.objects
            .all()
            .values("carmodel__model")
            .annotate(car_count=Count("carmodel"))
            .order_by("-car_count")
            .first()
        )
        top_seller = (
            RelationSell.objects
            .all()
            .values("seller__first_name", "seller__last_name", "seller__id")
            .annotate(car_count=Count("seller_id"))
            .order_by("-car_count")
            .first()
        )

        total_option_price = RelationSell.objects.aggregate(
            total_option=Sum(F("options__price"))
        )["total_option"] or 0

        total_model_price = RelationSell.objects.aggregate(
        total_model=Sum(F("carmodel__price"))
        )["total_model"] or 0

        total_sale_price = total_model_price + total_option_price

        # Response
        stats_data = {
            "top_selled_car": {
                "model": top_selled_car["carmodel__model"],
                "number": top_selled_car["car_count"],
            },
            "top_seller": {
                "id": top_seller["seller__id"],
                "name": f'{top_seller["seller__first_name"]} {top_seller["seller__last_name"]}',
                "number": top_seller["car_count"],
            },
            "total_sale_price": total_sale_price,
        }
        return Response(stats_data, status=status.HTTP_200_OK)
