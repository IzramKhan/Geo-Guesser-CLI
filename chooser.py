from picker import pick_country_from_world, pick_capital_from_world, pick_country_from_continent, pick_capital_from_continent
from utils.helpers import typing_effect
from viz.messages import Messages as msg

def choose_world_or_continent(countries=True) -> str:
    while True:
        choice = input('\nEnter 1 -> From World. 2 -> From Continent: ').strip()
        if choice == '1':
            if countries:
                return pick_country_from_world()
            return pick_capital_from_world()
        elif choice == '2':
            if countries:
                return pick_country_from_continent()
            return pick_capital_from_continent()
        else:
            typing_effect(msg.chooser_error)

def countries_or_capitals() -> str:
    options = {
        '1': lambda: choose_world_or_continent(),
        '2': lambda: choose_world_or_continent(countries=False)
    }

    while True:
        choice = input('\nEnter 1 -> Countries 2 -> Capitals: ').strip()
        if choice in options:
            return options[choice]()
        typing_effect(msg.chooser_error)
