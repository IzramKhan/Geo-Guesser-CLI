import string
from utils.helpers import typing_effect
from viz.messages import Messages as msg

def validate_guess(words_already_guessed_lst: list, guess_num: int) -> str:
    while True:
        guess = input(f'\nEnter your guess {guess_num}: ').lower().strip()
        
        if guess in words_already_guessed_lst:
            typing_effect(msg.word_already_guessed)

        elif guess == 'hint':
            return guess

        elif len(guess) == 1 and guess in string.ascii_lowercase:
            return guess

        else:
            typing_effect(msg.invalid_guess)

def handle_incorrect_guess(guess: str, random_entity: str, words_already_guessed_lst: list, incorrect_words: list) -> bool:
    words_already_guessed_lst.append(guess)
    
    if guess not in random_entity:
        incorrect_words.append(guess)
    
        typing_effect(msg.wrong_guess)
        # Returns True if the guess was wrong, False if it was correct.
        return True
    return False

def handle_correct_guess(guess: str, random_entity: str, random_entity_viz: list):
   
    for index, letter in enumerate(random_entity):
        if guess == letter:
            random_entity_viz[index] = guess.upper()
