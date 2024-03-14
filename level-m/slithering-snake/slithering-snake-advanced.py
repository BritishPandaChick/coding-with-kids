import random

#Phase 1 Code - Global variables
snake = []
snakeDx = 0
snakeDy = -1
game_over = False
background = stage.set_background_color("green")

# Phase 3 Global Variables - set up game variables
size = 10
segs = []

#Phase 4 Global variables - apple and apple positions
growth = 3
apple_x = random.randint(-24, 24)

apple_y = random.randint(-24, 24)
# Bonus Global Variables - poison apple and positions
papple_x = random.randint(-24, 24)
papple_y = random.randint(-24, 24)

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

# Bonus - Calculate and add head to list of snake positions
def add_head(head):
    global size
    snake_x = head[0] + snakeDx
    snake_y = head[1] + snakeDy
    snake.append((snake_x, snake_y))
    # get new head of the snake
    head = snake[len(snake) - 1]
    #draw new head 
    circle = codesters.Circle(head[0] * size, head[1] * size, size, "orange")
    #add new head to the list of snake sprites 
    segs.append(circle)
    
#Phase 5 - function that checks if the snake collides with the wall 
def check_state(head):
    global game_over 
    # check for snake hitting the walls 
    if head[0] > 25 or head[0] < -25 or head[1] > 25 or head[1] < -25:
        game_over = True 
    #Phase 6 - check for snake biting itself 
    for seg in snake:
        if seg is not head and head[0] == seg[0] and head[1] == seg[1]:
            game_over = True 
            break

#Phase 4 - Function that checks to see if snake collides with the apple
def check_apple(head, apple):
    global apple_x, apple_y, size, growth
    if head[0] == apple_x and head[1] == apple_y:
        #make new randomized coordinates for the apple
        apple_x = random.randint(-24, 24)
        apple_y = random.randint(-24, 24)
        #increase the growth of the snake 
        growth += 3

# Bonus - Add poison apple to code 
def check_papple(head, papple):
    global papple_x, papple_y, size, growth
    if head[0] == papple_x and head[1] == papple_y:
        # make new randomized coordinates for the poison apple 
        papple_x = random.randint(-24, 24)
        papple_y = random.randint(-24, 24)
        # shrink the growth of the snake 
        growth -= 2
        
# Bonus - Check if the snake is growing 
def check_grow():
    global growth
    # Check to see if the snake is growing. If so, let it grow.
    if growth > 0:
        growth -= 1
    #remove tail end of the snake from both lists and form the game screen
    else:
        snake.pop(0)
        stage.remove_sprite(segs[0])
        segs.pop(0)

# Bonus - Check if the snake is shrinking 
def check_shrink():
    global game_over, growth 
    # Check if growth is less than 0. Player has eaten poisoned apple and snake should shrink 
    while growth < 0:
        if len(snake) > 0:
            snake.pop(0)
            stage.remove_sprite(segs[0])
            segs.pop(0)
            growth += 1
        else:
            game_over = True 
            break
        
# Phase 3 - Main Game function and while loop
def main():
    global game_over, size 
    #Add first head to the list of snake positions
    snake.append((0,0))
    seg = snake[0]
    #draw first head 
    circle = codesters.Circle(seg[0] * size, seg[1] * size, size, "orange")
    # add first head to list of snake sprites 
    segs.append(circle)
    # Add apple sprites 
    apple = codesters.Circle(apple_x * size, apple_y * size, size, "red")
    papple = codesters.Circle(papple_x * size, papple_y * size, size, "purple")
    #main game loop 
    while game_over is False:
        #get head of the snake 
        head = snake[len(snake) - 1]
        #calculate and add a new head to the list of snake positions 
        add_head(head)
        new_head = snake[len(snake) - 1]
        #Phase 4-check to see if snake has eaten the apple
        check_apple(new_head, apple)
        # Bonus - check if snake is growing
        check_grow()
        # Bonus - check to see if snake has eaten a poisoned apple
        check_papple(new_head, papple)
        # Bonus - check to see if the snake is shrinking
        check_shrink()
        #Phase 5-check to see if snake has collided with the wall 
        check_state(new_head)
        #remove the previous apple and add a new one
        stage.remove_sprite(apple)
        apple = codesters.Circle(apple_x * size, apple_y * size, size, "red")
        #remove poisoned apple and add a new one
        stage.remove_sprite(papple)
        papple = codesters.Circle(papple_x * size, papple_y * size, size, "purple") 
        stage.wait(0.1)
    # Phase 5 - display text saying the game is over 
    text = codesters.Text("Game Over", 0, 0, "red")
    
# Call function
main()
