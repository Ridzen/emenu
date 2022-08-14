from django.contrib import admin
from .models import Basket
# Register your models here.


@admin.register(Basket)
class AdminCards(admin.ModelAdmin):
    pass