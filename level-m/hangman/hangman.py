#import libraries 
import random 

# Constants 
MAX_GUESSES = 6 

# Global Variables
secret_word = ''
letters_guessed = []

def get_word():
    words = ["apple", "orange", "python", "happy", "birthday", "random", "life", "string", "list"]
    word = random.choice(words)
    return word