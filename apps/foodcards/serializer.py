from rest_framework import serializers

from apps.foodcards.models import CardsCategories, Cards


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('__all__')

    def create(self, validated_data):
        return Cards.objects.create(**validated_data)


class CardsCategorySerializer(serializers.ModelSerializer):
    cards = CardsSerializer(many=True)

    class Meta:
        model = CardsCategories
        fields = "__all__"
