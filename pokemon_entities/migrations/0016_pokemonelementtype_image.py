# Generated by Django 3.1.14 on 2022-09-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20220910_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
