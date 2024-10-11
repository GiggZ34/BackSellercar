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
        fields = ["id", "seller", "carmodel", "customer", "options", ]


class PostRelationSellModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationSell
        fields = ["id", "seller", "carmodel", "customer", "options", ]
        read_only_fields = ["id", "seller"]
        extra_kwargs = {"options": {"required": False}}

    def validate(self, attrs):
        options = attrs.get("options", [])
        for option in options:
            if option.model != attrs["carmodel"]:
                raise serializers.ValidationError("Option models do not match")
        return super().validate(attrs)




