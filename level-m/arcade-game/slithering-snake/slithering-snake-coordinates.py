import random

#Phase 1 Code - Global variables
snake = []
snakeDx = 0
snakeDy = -1
game_over = False
background = stage.set_background_color("green")
#Phase 3 Global Variables - set up game variables
size = 10
segs = []
#Phase 4 Global variables 
growth = 3
appleCor = [random.randint(-24, 24), random.randint(-24, 24)]
#Bonus Global Variables
pappleCor = [random.randint(-24, 24), random.randint(-24, 24)]

# Phase 2 Code 
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

# Bonus - Calculate and add head to the list of snake positions
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
    global appleCor, size, growth
    if head[0] == appleCor[0] and head[1] == appleCor[1]:
        #make new randomized coordinates for the apple
        appleCor[0] = random.randint(-24, 24)
        appleCor[1] = random.randint(-24, 24)
        #increase the growth of the snake 
        growth += 3

# Bonus - Function that checks snake collides with poisoned apple 
def check_papple(head, papple):
    global pappleCor, size, growth
    if head[0] == pappleCor[0] and head[1] == pappleCor[1]:
        #make new randomized coordinates for the apple
        pappleCor[0] = random.randint(-24, 24)
        pappleCor[1] = random.randint(-24, 24)
        #increase the growth of the snake 
        growth -= 2
        
# Bonus - Check to see if snake is growing
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
            
# Bonus - Check to see if snake is shrinking
def check_shrink():
    global game_over, growth 
    # Check if growth is less than 0. Player has eaten poisoned apple and snake should shrink 
    while growth < 0:
        if len(snake) > 0:
            snake.pop(0)
            stage.remove_sprite(segs[0])
            segs.pop()
            growth += 1
        else:
            game_over = True 
            break
        
# Phase 3 - Main game function
def main():
    #global variables 
    global game_over, size
    #Add first head to the list of snake positions
    snake.append((0,0))
    seg = snake[0]
    #draw first head 
    circle = codesters.Circle(seg[0] * size, seg[1] * size, size, "orange")
    # add first head to list of snake sprites 
    segs.append(circle)
    # Add apple sprites 
    apple = codesters.Circle(appleCor[0] * size, appleCor[1] * size, size, "red")
    papple = codesters.Circle(appleCor[0] * size, appleCor[1] * size, size, "purple")
    
    #main game loop 
    while game_over is False:
        #get head of the snake 
        head = snake[len(snake) - 1]
        #calculate and add a new head to the list of snake positions 
        add_head(head)
        new_head = snake[len(snake) - 1]
        #Phase 4-check to see if snake has eaten the apple
        check_apple(new_head, apple)
        #Bonus - check to see if snake is growing
        check_grow()
        # Bonus - check to see if snake eats poisoned apple 
        check_papple(new_head, papple)
        #Bonus - check to see if the snake shrinks
        check_shrink()
        #Phase 5-check to see if snake has collided with the wall 
        check_state(new_head)
        # Remove apple and add a new one 
        stage.remove_sprite(apple)
        #add new apple 
        apple = codesters.Circle(appleCor[0] * size, appleCor[1] * size, size, "red")
        # Remove poisoned apple and add a new one 
        stage.remove_sprite(papple)
        #add new apple 
        papple = codesters.Circle(pappleCor[0] * size, pappleCor[1] * size, size, "purple")
        stage.wait(0.1)
    # Phase 5 - display text saying the game is over 
    text = codesters.Text("Game Over", 0, 0, "red")
    
# Call function
main()