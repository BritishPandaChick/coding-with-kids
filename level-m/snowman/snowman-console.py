# Phase 1 Code - Setup 
word = ''
display_word = []
guesses = 6
guessed = ''

def init():
    global guesses, guessed, word, display_word
    words = ["camel", "horse", "coding", "debugging", "python", "lucky", "mississippi"]
    word = random.choice(words)
    display_word = ["_"]*len(word)
    guesses = 6
    guessed = ''
    
def word_guessed():
    return "_" not in display_word
    
def main():
    global guesses, guessed
    init()
    # Phase 2 Code - Guessing letters
    print(" ".join(l for l in display_word))
    while not word_guessed() and guesses > 0:
        letter = input("Guess a letter: ")
        # Phase 3 code - Validating inputs
        if len(letter) != 1:
            print('Please enter one letter at time')
            continue
        elif letter in guessed:
            print('You already tried "' +letter+'" guess again')
            continue
        # End of Phase 3 code
        guessed += letter
        if letter not in word:
            guesses -= 1
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter 
        print(" ".join(l for l in display_word))
        print("Letters guessed: "+guessed)
        print("Guesses left: {}".format(guesses))
    if guesses > 0:
        print("You guessed it!")
    else:
        print("Better luck next time")
    
main()