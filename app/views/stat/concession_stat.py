from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import RelationSell
from app.serializers import RelationSellModelSerializer


class ConcessionStatView(APIView):
    def get(self, request, concession_id, *args, **kwargs):

        # Get data
        sale_of_concession = RelationSell.objects.filter(seller__concession_id=concession_id)
        total_sale_all = RelationSell.objects.all()

        best_selled_car_list = (
            RelationSell.objects
            .filter(seller__concession_id=concession_id)
            .values("carmodel__model")
            .annotate(car_count=Count("carmodel"))
            .order_by("-car_count")
        )

        best_seller_of_concession = (
            RelationSell.objects
            .filter(seller__concession_id=concession_id)
            .values("seller__first_name", "seller__last_name")
            .annotate(car_count=Count("seller_id"))
            .order_by("-car_count")
            .first()
        )

        # Serialize data
        serialized_sale_of_concession = RelationSellModelSerializer(sale_of_concession, many=True).data
        serialized_total_sale_all = RelationSellModelSerializer(total_sale_all, many=True).data

        if len(serialized_sale_of_concession) < 1:
            stats_data = {
                "error": "pas de vente"
            }
            return Response(stats_data, status=status.HTTP_200_OK)

        else:
            # Calcul
            total_selled_in_concession = len(serialized_sale_of_concession)
            total_selled_all = round((len(serialized_sale_of_concession) * 100) / len(serialized_total_sale_all))

            stats_data = {
                "car_selled": {
                   "most_selled_car":{
                       "model": best_selled_car_list[0]["carmodel__model"],
                       "total": best_selled_car_list[0]["car_count"],
                   },
                   "detail_car_selled": best_selled_car_list,
                   "total_selled": total_selled_in_concession
                },
                "best_seller": {
                    "full_name": f'{best_seller_of_concession["seller__first_name"]} {best_seller_of_concession["seller__last_name"]}',
                    "number_of_sale": best_seller_of_concession["car_count"],
                },
                "purcent_of_total_selled": f'{total_selled_all}%',

            }
            return Response(stats_data, status=status.HTTP_200_OK)
