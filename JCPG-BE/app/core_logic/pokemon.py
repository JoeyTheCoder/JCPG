import numbers
import requests
import json
import typing

import random




def getPokemon(item_id: int):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + item_id),
    pokemonOutput = json.loads(response[0].text)
    return pokemonOutput