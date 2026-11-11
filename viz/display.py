
from utils.helpers import typing_effect
from time import sleep

def display_random_entity(random_entity_viz: list, incorrect_words_lst: list, lives: int) -> None:
    print('\n' + '-' * 75)
    
    for rev in random_entity_viz:
        print(rev.upper(), end=' ')
    print(f'\n\nWrong guesses: {incorrect_words_lst}')
    print(f'Lives left: {lives}')
    print('\n' + '-' * 75)

def intro():
    typing_effect('\n||  *  |  **  WELCOME TO GEO-GUESSER CLI  **  |  *  ||\n')
    sleep(1)

def outro():
    typing_effect('\n||  *  |  ** THANK\'S FOR PLAYING  **  |  *  ||\n')

def display_win():
    typing_effect('\n||  *  |  ** CONGRATS YOU WON THIS ROUND  **  |  *  ||\n')
    sleep(1)

def display_lost(random_entity: str) -> None:
    typing_effect('\n||  *  |  ** YOU LOST! TRY AGAIN  **  |  *  ||\n')
    print(f'The answer was: {random_entity.replace("-", " ").upper()}')
    sleep(1)

def manual():
    print('''
HELLO AND WELCOME TO CLI GEO-GUESSER!

1. You can choose either countries or capitals to guess.
2. You can choose to guess from entire world or specific continent.
3. HINT: By entering 'hint' a random blank will be filled with alphabet (only once per round)
4. You have five lives to guess. Guess before your lives run out
5. After each round you will be asked whether you want to play another round or not.
          ''')

def display_round_num(round_num: int) -> None:
    typing_effect(f'\nROUND NUMBER: {round_num}\n')
