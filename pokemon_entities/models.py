from django.db import models


class Pokemon(models.Model):
    text = models.CharField(max_length=200)
    text_en = models.CharField(max_length=200, blank=True)
    text_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.text


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_DEFAULT, default=1, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.pokemon}: {self.lat} - {self.lon}'
