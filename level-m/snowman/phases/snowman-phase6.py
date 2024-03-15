asker = codesters.Sprite("robot", 100, -200)
guessed_display = codesters.Text("Letters Guessed:", -160, -100, "black")
t = turtle.Turtle() #add phase 6
t.penup() # add phase 6
t.hide() # add phase 6
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

def word_guessed():
    return "_" not in display_word

# Phase 6 code - update_snowman function
def update_snowman():
    if guesses == 5:
        t.goto(100, 160)
        t.pendown()
        t.circle(20)
    elif guesses == 4:
        t.goto(100, 100)
        t.pendown()
        t.circle(30)
    elif guesses == 3:
        t.goto(100, 20)
        t.pendown()
        t.circle(40)
    elif guesses == 2:
        t.goto(130, 140)
        t.pendown()
        t.goto(160, 160)
    elif guesses == 1:
        t.goto(70, 140)
        t.pendown()
        t.goto(30, 160)
    elif guesses == 0:
        t.goto(80, 200)
        t.pendown()
        t.goto(120, 200)
        t.goto(90, 200)
        for i in range(4):
            t.forward(20)
            t.left(90)
    t.penup()
 
def main():
    global guesses, guessed
    init()
    while not word_guessed() and guesses > 0:
        letter = asker.ask("Guess a letter: ")
        if len(letter) != 1:
            asker.say('Please enter one letter at a time')
            stage.wait(1)
            continue
        elif letter in guessed:
            asker.say('You already tried "'+letter+'" guess again')
            stage.wait(1)
            continue
        guessed += letter
        if letter not in word:
            guesses -= 1
            update_snowman() # add phase 6
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter
        update_display()
    if guesses > 0:
        asker.say("You guessed it!")
    else:
        asker.say("Better luck next time")

main()