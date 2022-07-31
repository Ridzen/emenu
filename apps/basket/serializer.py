from rest_framework import serializers

from apps.basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('__all__')

    def create(self, validated_data):
        return Basket.objects.create(**validated_data)
