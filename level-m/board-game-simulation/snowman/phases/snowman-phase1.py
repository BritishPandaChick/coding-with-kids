word = ''
display_word = []
guesses = 6
guessed = ''

def init():
    global guesses, guessed, word, display_word 
    words = ["camel", "horse", "coding", "debugging", "python", "mississippi"]
    word = random.choice(words)
    display_word = ["_"] * len(word)
    guesses = 6
    guessed = ''
    
def main():
    init()

main()