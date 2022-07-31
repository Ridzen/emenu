# Generated by Django 4.0.6 on 2022-07-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcards', '0004_alter_cards_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
    ]