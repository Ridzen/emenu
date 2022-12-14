# Generated by Django 4.0.6 on 2022-07-24 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodcards', '0002_postcategories_alter_cards_image_alter_cards_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('list_food', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='foodcards.cards')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'db_table': 'basket_db',
            },
        ),
    ]
