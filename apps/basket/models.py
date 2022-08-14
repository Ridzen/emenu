from django.db import models
from apps.foodcards.models import Cards


# Create your models here.


class Basket(models.Model):
    """Модель Корзины"""

    list_food = models.ForeignKey(
        to=Cards, on_delete=models.CASCADE, related_name='name',
                                  default=None, null=True
    )
    full_price = models.ForeignKey(
        to=Cards, on_delete=models.CASCADE, related_name='full_price',
                                  default=None, null=True
    )
    comments = models.TextField()

    class Meta:
        db_table = 'basket_db'
        verbose_name_plural = 'Корзины'
        verbose_name = "Корзина"

    def __str__(self):
        return self.list_food
