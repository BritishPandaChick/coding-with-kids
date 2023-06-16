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
    global guessed
    init()
    print(" ".join(l for l in display_word))
    while True:
        letter = input("Guess a letter: ")
        guessed += letter
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
        print(" ".join(l for l in display_word))
        print("Letters guessed: "+guessed)

main()