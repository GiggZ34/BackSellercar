from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import RelationSell, Seller
from app.serializers import RelationSellModelSerializer


def total_revenue_calculator(sale_of_user):
    total = 0

    for sale in sale_of_user:
        if len(sale["options"]) > 1:
            for option in sale["options"]:
                total += option["price"]
        total += sale["carmodel"]["price"]

    return total


class SellerSaleStatView(APIView):
    def get(self, request, seller_id, *args, **kwargs):

        # Get data
        info_user = Seller.objects.get(id=seller_id)
        user_sale = RelationSell.objects.filter(seller__id=seller_id)
        all_sale = RelationSell.objects.all()
        user_concession_sale = RelationSell.objects.filter(seller__concession_id=info_user.concession_id)

        best_selled_car = (
            RelationSell.objects
            .filter(seller__id=seller_id)
            .values("carmodel__model")
            .annotate(car_count=Count("carmodel"))
            .order_by("-car_count")
            .first()
        )

        # Serialize data
        serialized_user_data = RelationSellModelSerializer(user_sale, many=True).data
        serialized_all_data = RelationSellModelSerializer(all_sale, many=True).data
        serialized_concession_data = RelationSellModelSerializer(user_concession_sale, many=True).data

        # Calcul
        number_sale_user = len(serialized_user_data)
        number_sale_all = len(serialized_all_data)
        number_sale_concession = len(serialized_concession_data)

        if number_sale_user <= 0:
            stats_data = {
                "error": "pas de vente"
            }
            return Response(stats_data, status=status.HTTP_200_OK)

        else:
            purcent_sale_user_total = round((number_sale_user * 100) / number_sale_all)
            purcent_sale_user_concession = round((number_sale_user * 100) / number_sale_concession)

            moy_options = sum(len(option["options"]) for option in serialized_user_data)

            total_revenue = total_revenue_calculator(serialized_user_data)

            stats_data = {
                "purcent_sale_total": f'{purcent_sale_user_total}%',
                "purcent_in_concession": f'{purcent_sale_user_concession}%',
                "moy_option_per_car": f'{moy_options}',
                "best_sale_car": {
                   "model": best_selled_car["carmodel__model"],
                   "number_selled": best_selled_car["car_count"],
                },
                "total_revenue": f'{total_revenue}€'
            }
            return Response(stats_data, status=status.HTTP_200_OK)

