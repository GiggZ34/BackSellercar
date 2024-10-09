from rest_framework import serializers
from app.constantes import SellerRoles
from app.models import Seller


class SellerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ["id", "roles", "first_name", "last_name", "username", "concession"]

    def validate_roles(self, value):
        user: Seller = self.context["request"].user

        if value != SellerRoles.STANDARD and (user.is_anonymous or user.roles != SellerRoles.ELON):
            raise serializers.ValidationError("Role not allow")
        return value
