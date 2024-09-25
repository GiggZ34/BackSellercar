from rest_framework import serializers

from app.models import RelationSell


class RelationSellModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationSell
        fields = ["seller", "carmodel", "customer", "options"]
