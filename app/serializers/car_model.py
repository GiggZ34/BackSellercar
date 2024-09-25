from rest_framework import serializers

from app.models import CarModel


class CartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["model", "price"]
