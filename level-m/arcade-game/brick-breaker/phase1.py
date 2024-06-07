# global variables
score = 0
rows = 4
columns = 8
bricks = []

# score display
display = codesters.Text("Score: 0", 0, 235, "red")

# setup sprites
player = codesters.Rectangle(0, -220, 80, 15, "red")
player.lives = 3
ball = codesters.Circle(0, 0, 20, "blue")

# paddle controls
def left():
    player.move_left(15)
stage.event_key("a", left)

def right():
    player.move_right(15)
stage.event_key("d", right)