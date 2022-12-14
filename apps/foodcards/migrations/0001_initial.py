# Generated by Django 4.0.6 on 2022-07-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('amount', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'db_table': 'posts_db',
            },
        ),
    ]
