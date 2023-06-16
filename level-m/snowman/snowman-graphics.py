asker = codester.Sprite("robot", 100, -200)
guessed_display = codesters.Text("Letters Guessed:", -160, -100, "black")
display = []
word = ''
display_word = []
guesses = 6
guessed = ''

def init():
    global guesses, guessed, word, display_word, display
    words = ["camel", "horse", "coding", "debugging", "python", "mississippi"]
    word = random.choice(words)
    display_word = ["_"]*len(word)
    guesses = 6
    guessed = ''
    display = []
    for i in range(len(display_word)):
        display.append(codesters.Text(display_word[i], -230+i*25, 50, "red"))
        guessed_display.set_text("Letters Guessed:")

def update_display():
    for i in range(len(display_word)):
        display[i].set_text(display_word[i])
    guessed_display.set_text("Letters Guessed:\n{}".format(guessed))
    
def main():
    global guesses, guessed
    init()
    print(" ".join(l for l in display_word))
    while not word_guessed() and guesses > 0:
        letter = asker.ask("Guess a letter: ")
        if len(letter) != 1:
            asker.say('Please enter one letter at a time')
            stage.wait(1)
        elif letter in guessed:
            asker.say('You already tried "'+letter+'" guess again')
            stage.wait(1)
        guessed += letter
        if letter not in word:
            guesses -= 1
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter
        update_display()
    if guesses > 0:
        print("You guessed it!")
    else:
        print("Better luck next time")

main()