import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    datetime_now = timezone.localtime(timezone.now())
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=datetime_now,
        disappeared_at__gt=datetime_now
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        pokemon = pokemon_entity.pokemon
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.text,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    object_pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon = {
        "title_ru": object_pokemon.text,
        "title_en": object_pokemon.text_en,
        "title_jp": object_pokemon.text_jp,
        "img_url": request.build_absolute_uri(object_pokemon.image.url),
        "description": object_pokemon.description
    }
    if object_pokemon.previous_evolution:
        pokemon["previous_evolution"] = {
            "pokemon_id": object_pokemon.previous_evolution.pk,
            "title_ru": object_pokemon.previous_evolution.text,
            "img_url": request.build_absolute_uri(object_pokemon.previous_evolution.image.url)
        }
    next_evolution = Pokemon.objects.filter(previous_evolution=object_pokemon)
    if next_evolution:
        pokemon["next_evolution"] = {
            "pokemon_id": next_evolution[0].pk,
            "title_ru": next_evolution[0].text,
            "img_url": request.build_absolute_uri(next_evolution[0].image.url)
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    datetime_now = timezone.localtime(timezone.now())
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=object_pokemon,
        appeared_at__lt=datetime_now,
        disappeared_at__gt=datetime_now
    )
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(object_pokemon.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
