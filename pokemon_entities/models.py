from django.db import models


class Pokemon(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.text


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str_(self):
        return f'{self.lat} - {self.lon}'
