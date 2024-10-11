from django.db.models import Count, F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.commons.db_functions import SubquerySum
from app.models import RelationSell, Concession


class GeneralStatView(APIView):
    def get(self, request, *args, **kwargs):

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
            .values("seller__first_name", "seller__last_name")
            .annotate(car_count=Count("seller_id"))
            .order_by("-car_count")
            .first()
        )

        # total_sale_price = Concession.objects.annotate(
        #     number_sale_all_price=SubquerySum(RelationSell.objects.values(value=F("carmodel__price"))) + SubquerySum(
        #         RelationSell.objects.values(value=F("options__price"))),
        # )

        # Response
        stats_data = {
            "top_selled_car": {
                "model": top_selled_car["carmodel__model"],
                "number": top_selled_car["car_count"],
                },
            "top_seller": {
                "name": f'{top_seller["seller__first_name"]} {top_seller["seller__last_name"]}',
                "number_of_sales": top_seller["car_count"],
            },
            # "total_sale_price": total_sale_price,

        }

        return Response(stats_data, status=status.HTTP_200_OK)
