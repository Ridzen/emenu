from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class CardsCategories(models.Model):

    """Модель для категории карточек еды"""

    title = models.CharField(
        max_length=255, unique=False
    )
    description = RichTextUploadingField()
    price = models.DecimalField(
        decimal_places=10, max_digits=15, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = 'Категории постов'
        verbose_name = 'Категория поста'

    def __str__(self):
        return self.title


class Cards(models.Model):

    """ Модель для Карточек Еды """

    title = models.CharField(
        max_length=255
    )
    image = models.ImageField(
        help_text="An image or logo for this Card (optional)",
                              blank=True, null=True
    )
    description = RichTextUploadingField()
    price = models.DecimalField(
        decimal_places=10, max_digits=15, null=True, blank=True
    )
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(
        to=CardsCategories, on_delete=models.CASCADE, related_name='cards',
        default=None, null=True
    )
    in_basket = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = 'cards_db'
        verbose_name_plural = 'Карточки'
        verbose_name = "Карточка"

    def __str__(self):
        return self.title
