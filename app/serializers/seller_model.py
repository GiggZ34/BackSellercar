from rest_framework import serializers

from app.models import Seller


class SellerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ["roles", "concession"]
