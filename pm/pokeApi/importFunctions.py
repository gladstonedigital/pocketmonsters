import json
import requests

api_url_base = 'https://pokeapi.co/api/v2/'

def getPokemon(pokemonid):
    
    endpoint = api_url_base+'pokemon/'+pokemonid
    r = requests.get(endpoint)
    data = r.json()

    return data
