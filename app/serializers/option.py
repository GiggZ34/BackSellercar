from rest_framework import serializers

from app.models.option import Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["model", "title", "price"]