from rest_framework import serializers

from app.models import RelationSell
from app.serializers.car_model import CarModelSerializer
from app.serializers.customer import CustomerSerializer
from app.serializers.option import OptionSerializer
from app.serializers.seller_model import SellerModelSerializer


class RelationSellModelSerializer(serializers.ModelSerializer):
    seller = SellerModelSerializer()
    carmodel = CarModelSerializer()
    customer = CustomerSerializer()
    options = OptionSerializer(many=True)

    class Meta:
        model = RelationSell
        fields = ["seller", "carmodel", "customer", "options", ]


