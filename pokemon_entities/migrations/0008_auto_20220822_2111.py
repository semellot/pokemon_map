# Generated by Django 3.1.14 on 2022-08-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='text_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='text_jp',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
