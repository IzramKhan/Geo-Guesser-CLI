import random
from data import countries, capitals
from utils.helpers import typing_effect
from viz.messages import Messages as msg

def pick_country_from_world() -> str:
    return random.choice(countries.world_countries)

def pick_country_from_continent() -> str:
    continents = {
        'asia': countries.asia_countries,
        'europe': countries.europe_countries,
        'africa': countries.africa_countries,
        'north_america': countries.north_america_countries,
        'south_america': countries.south_america_countries,
        'oceania': countries.oceania_countries
    }

    while True:
        continent = input('\nEnter Continent: ').lower().strip().replace(' ', '_')

        if continent in continents:
            return random.choice(continents[continent])
        elif continent == 'antarctica':
            typing_effect(msg.antartica)
        else:
            typing_effect(msg.wrong_continent)

def pick_capital_from_world() -> str:
    return random.choice(capitals.world_capitals)

def pick_capital_from_continent() -> str:
    continents = {
        'asia': capitals.asia_capitals,
        'europe': capitals.europe_capitals,
        'africa': capitals.africa_capitals,
        'north_america': capitals.north_america_capitals,
        'south_america': capitals.south_america_capitals,
        'oceania': capitals.oceania_capitals
    }

    while True:
        continent = input('\nEnter Continent: ').lower().strip().replace(' ', '_')

        if continent in continents:
            return random.choice(continents[continent])
        elif continent == 'antarctica':
            typing_effect(msg.antartica)
        else:
            typing_effect(msg.wrong_continent)
