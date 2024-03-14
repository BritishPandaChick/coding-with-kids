# list of snake positions
snake = []

#tells the snake what direction to move in
snakeDx = 0
snakeDy = -1

# Determine if the game is over
game_over = False

# background for project
background = stage.set_background_color("green")

# Phase 2 Code - Player Controls
def up_key():
    global snakeDx, snakeDy 
    snakeDx = 0 
    snakeDy = 1
stage.event_key("up", up_key)

def down_key():
    global snakeDx, snakeDy
    snakeDx = 0 
    snakeDy = -1 
stage.event_key("down", down_key)

def left_key():
    global snakeDx, snakeDy 
    snakeDx = -1 
    snakeDy = 0 
stage.event_key("left", left_key)

def right_key():
    global snakeDx, snakeDy 
    snakeDx = 1 
    snakeDy = 0 
stage.event_key("right", right_key)