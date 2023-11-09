word = ''
display_word = []
guesses = 6
guessed = ''

def init():
    global guesses, guessed, word, display_word 
    words = ["camel", "horse", "coding", "debugging", "python", "mississippi"]
    word = random.choice(words)
    display_word = ["_"]*len(word)
    guesses = 6
    guessed = ''
    
def main():
    global guessed
    init()
    print(" ".join(l for l in display_word))
    while True:
        letter = input("Guess a letter: ")
        if len(letter) != 1:
            print('Please enter one letter at a time')
            continue
        elif letter in guessed:
            print('You already tried "'+letter+'" guess again')
            continue
        guessed += letter
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
        print(" ".join(l for l in display_word))
        print("Letters guessed: "+guessed)

main()