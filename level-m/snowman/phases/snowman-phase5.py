asker = codesters.Sprite("robot", 100, -200)
guessed_display = codesters.Text("Letters Guessed:", -160, -100, "black")
display = []

# original global variables 
word = ''
display_word = []
guesses = 6
guessed = ''

def init():
    global guesses, guessed, word, display_word, display # add phase 5 display
    words = ["camel", "horse", "coding", "debugging", "python", "mississippi"]
    word = random.choice(words)
    display_word = ["_"]*len(word)
    guesses = 6
    guessed = ''
    
    # Phase 5 code 
    display = []
    for i in range(len(display_word)):
        display.append(codesters.Text(display_word[i], -230+i*25, 50, "red"))
        guessed_display.set_text("Letters Guessed:")

def word_guessed():
    return "_" not in display_word

# Phase 5 code 
def update_display():
    for i in range(len(display_word)):
        display[i].set_text(display_word[i])
    guessed_display.set_text("Letters Guessed:\n{}".format(guessed))
    
def main():
    global guesses, guessed
    init()
    while not word_guessed() and guesses > 0:
        letter = asker.ask("Guess a letter: ") # add phase 5
        if len(letter) != 1:
            asker.say('Please enter one letter at a time') # add phase 5
            stage.wait(1)
            continue
        elif letter in guessed:
            asker.say('You already tried "'+letter+'" guess again') # add phase 5
            stage.wait(1)
            continue
        guessed += letter
        if letter not in word:
            guesses -= 1
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter
        update_display() # add phase 5 code 
    if guesses > 0:
        asker.say("You guessed it!") # phase 5 code
    else:
        asker.say("Better luck next time") # phase 5 code

main()