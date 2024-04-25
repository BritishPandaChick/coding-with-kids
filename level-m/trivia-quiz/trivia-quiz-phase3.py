stage.set_background_color("black")

# six text sprites
question = codesters.Text("test", 0, 180, "lightblue")
a = codesters.Text("A:", -150, 50, "lightblue")
b = codesters.Text("B:", 150, 50, "lightblue")
c = codesters.Text("C:", -150, -50, "lightblue")
d = codesters.Text("D:", 150, -50, "lightblue")
display = codesters.Text(" ", 0, 100, "lightblue")

choices = [a,b,c,d]

# parallel lists to store components of a question
questions = []

# each element is a list of possible answers a,b,c, and d
answers = []

# each element is a reference to a text sprite
correct_answers = []

# Added in Phase 3
question_num = 0
score = 0

# Phase 2 - adding questions to the game
def create_questions():
    #question 1
    questions.append("Link is a character from which game series?")
    answers.append(["Tomb Raider", "Legend of Zelda", "Super Mario Bros", "Pokemon"])
    correct_answers.append(b)
    
    #question 2
    questions.append("Who was the first computer programmer?")
    answers.append(["Ada Lovelace", "Charles Babbage", "Grace Hopper", "Alan Turing"])
    correct_answers.append(a)
    
    #question 3
    questions.append("What  is 'pixel' short for?")
    answers.append(["pixel - it's not \nshort for anything", "Edward Pixelli", "pixelized point", "picture element"])
    correct_answers.append(d)

# Phase 3 - ask questions and checking the answer 
def ask_questions():
    question.set_text(questions[question_num])
    a.set_text("A: "+answers[question_num][0])
    b.set_text("B: "+answers[question_num][1])
    c.set_text("C: "+answers[question_num][2])
    d.set_text("D: "+answers[question_num][3])
    
def answer_click(choice):
    global score
    if choice is correct_answers[question_num]:
        display.set_text("Correct!")
        score += 1
    else:
        display.set_text("Incorrect")

for choice in choices:
    choice.event_click(answer_click)
    
def main():
    create_questions()
    ask_questions() # add phase 3
main()