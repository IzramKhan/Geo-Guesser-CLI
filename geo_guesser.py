from chooser import countries_or_capitals
from utils.helpers import lives_zero, no_underscores, get_hint
from utils.validators import validate_guess, handle_correct_guess, handle_incorrect_guess
from viz.display import intro, display_win, display_lost, display_random_entity, display_round_num, manual

def guesser(round_num):

    intro()
    manual()

    random_entity = countries_or_capitals()
    random_entity_viz = ['_' if ch != '-' else ' ' for ch in random_entity]
    words_already_guessed = []
    incorrect_guesses = []

    lives = 5
    hints = 0
    guess_num = 1
    
    display_round_num(round_num)

    while True:
        round_num += 1
        display_random_entity(random_entity_viz=random_entity_viz,
                              incorrect_words_lst=incorrect_guesses,
                              lives=lives
        )

        if lives_zero(lives=lives):
            return display_lost(random_entity=random_entity)

        if no_underscores(random_entity_viz):
            return display_win()

        guess = validate_guess(
            words_already_guessed_lst=words_already_guessed,
            guess_num=guess_num
        )
        
        
        if guess == 'hint':
            get_hint(
                random_entity=random_entity,
                random_entity_viz=random_entity_viz,
                hints=hints
            )
            hints += 1
            continue
        
        guess_num += 1
        
        if handle_incorrect_guess(
                guess=guess,
                random_entity=random_entity,
                words_already_guessed_lst=words_already_guessed,
                incorrect_words=incorrect_guesses
        ):
            lives -= 1  
            print(f'Words already guessed: {words_already_guessed}')
            continue

        handle_correct_guess(
            guess=guess,
            random_entity=random_entity,
            random_entity_viz=random_entity_viz,
        )

        print(f'Words already guessed: {words_already_guessed}')
