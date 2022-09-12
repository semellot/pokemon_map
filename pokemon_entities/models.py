from django.db import models


class PokemonElementType(models.Model):
    """Стихия покемона"""
    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(blank=True, verbose_name="Изображение")
    strong_against = models.ManyToManyField("self", blank=True, related_name="strong_against_elements", verbose_name="Силён против", symmetrical=False)

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    """Покемон"""
    name = models.CharField(max_length=200, verbose_name="Название")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="Название (EN)")
    name_jp = models.CharField(max_length=200, blank=True, verbose_name="Название (JP)")
    image = models.ImageField(blank=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    element_types = models.ManyToManyField(PokemonElementType, related_name="elements", verbose_name="Стихия")
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Предыдушая эволюция", related_name="prev_evolutions")

    def __str__(self):
        return self.text


class PokemonEntity(models.Model):
    """Сущность покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL,
        null=True, related_name="pokemons", verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Координата широты")
    lon = models.FloatField(verbose_name="Координата долготы")
    appeared_at = models.DateTimeField(null=True, verbose_name="Дата и время появления")
    disappeared_at = models.DateTimeField(null=True, verbose_name="Дата и время исчезновения")
    level = models.IntegerField(blank=True, verbose_name="Уровень")
    health = models.IntegerField(blank=True, verbose_name="Здоровье")
    strength = models.IntegerField(blank=True, verbose_name="Сила")
    defence = models.IntegerField(blank=True, verbose_name="Защита")
    stamina = models.IntegerField(blank=True, verbose_name="Выносливость")

    def __str__(self):
        return f'{self.pokemon}: {self.lat} - {self.lon}'
