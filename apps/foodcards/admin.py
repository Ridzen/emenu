from django.contrib import admin
from apps.foodcards.models import Cards, CardsCategories
# Register your models here.


@admin.register(Cards)
class AdminCards(admin.ModelAdmin):
    pass


@admin.register(CardsCategories)
class AdminCards(admin.ModelAdmin):
    pass
