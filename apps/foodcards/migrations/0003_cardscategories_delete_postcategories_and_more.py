# Generated by Django 4.0.6 on 2022-07-31 17:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcards', '0002_postcategories_alter_cards_image_alter_cards_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
            options={
                'verbose_name': 'Категория поста',
                'verbose_name_plural': 'Категории постов',
            },
        ),
        migrations.DeleteModel(
            name='PostCategories',
        ),
        migrations.AddField(
            model_name='cards',
            name='in_basket',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cards',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AddField(
            model_name='cards',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='foodcards.cardscategories'),
        ),
    ]