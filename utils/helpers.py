import time
from time import sleep
from viz.messages import Messages as msg
import random

def lives_zero(lives: int) -> bool:
    return lives == 0

def no_underscores(random_entity_viz: list) -> bool:
    return '_' not in random_entity_viz

def get_hint(random_entity: str, random_entity_viz: list, hints: int) -> None:
    if hints > 0:
        typing_effect(msg.hint_already_used)
        return

    # OLD VERSION
    # for index, (re, rev) in enumerate(zip(random_entity, random_entity_viz)):
    #     if rev == '_':
    #         random_entity_viz[index] = re
    #         break
    
    # NEW VERSION
    blanks = [i for i, ch in enumerate(random_entity_viz) if ch == '_']
    index = random.choice(blanks)
    random_entity_viz[index] = random_entity[index]

def typing_effect(text: str) -> None:
    for t in text:
        print(t, end='', flush=True)
        sleep(0.03)
    time.sleep(0.5)
    print()
    
def play_again() -> bool:
    while True:
        choice = input('\nWant to play again (y/n): ').lower().strip()
        return choice in ['y', 'yes']
