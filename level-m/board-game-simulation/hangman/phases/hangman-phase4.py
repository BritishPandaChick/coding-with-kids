#import libraries 
import random 

# Constants 
MAX_GUESSES = 6 

# Global Variables
secret_word = ''
letters_guessed = []

# Phase 2 - Choose a random word 
def get_word():
    words = ["apple", "orange", "python", "happy", "birthday", "random", "life", "string", "list"]
    word = random.choice(words)
    return word

# Phase 3 - check if word has been guessed
def word_guessed():
    # Set up variables 
    global secret_word, letters_guessed

    for letter in secret_word:
        if not (letter in letters_guessed):
            return False
    return True
    
# Phase 4 - Printing Guess
def print_guessed():
    global secret_word, letters_guessed
    guessed_word = []
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("-")
    print("".join(guessed_word))