#import libraries 
import random 

# Constants 
MAX_GUESSES = 6 

# Global Variables
secret_word = ''
letters_guessed = []

def get_word():
    words = []
    in_file = open("wordlist.txt", "r")
    for line in in_file:
        words.append(line.strip())
    word = random.choice(words)
    return word