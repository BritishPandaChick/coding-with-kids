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