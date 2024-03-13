stage.set_background_color("green")

def create_ball():
    ball = codesters.Circle(-200, 200, 50, "red")
    ball.set_x_speed(random.randint(1, 7))
    ball.set_y_speed(random.randint(1, 7))
    
def play(number):
    for ball in range(int(number)):
        create_ball()
        
count = stage.ask("How Many Ball Groups (4 balls per group)???")

if count == "":
    text = codesters.Text("Type in a number! Blank is not allowed! Play again.", 0, 125)
else:
    play(count)