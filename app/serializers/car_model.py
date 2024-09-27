from rest_framework import serializers

from app.models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["id", "model", "price"]


class PostCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["id", "model", "price"]
        read_only_fields = ["id"]
