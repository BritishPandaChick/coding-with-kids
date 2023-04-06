# Phase 1 - Global Variables 
snake = [] # list of snake positions
snakeDx = 0 # Tells snake what direction to move in
snakeDy = -1
game_over = False # Determine if the game is over
background = stage.set_background_color("green") # background for project

# Phase 2 - Player Controls
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