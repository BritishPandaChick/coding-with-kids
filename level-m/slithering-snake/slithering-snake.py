import random 

# Phase 1 - Global Variables 
snake = [] # list of snake positions
snakeDx = 0 # Tells snake what direction to move in
snakeDy = -1
game_over = False # Determine if the game is over
background = stage.set_background_color("green") # background for project
#Phase 4 Global variables 
growth = 3
appleCor = [random.randint(-24, 24), random.randint(-24, 24)]
apple = codesters.Circle(appleCor[0] * 10, appleCor[1] * 10, 10, "red")

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

#Phase 5 - function that checks if the snake collides with the wall 
def check_state(head):
    global game_over 
    # check for snake hitting the walls 
    if head[0] > 25 or head[0] < -25 or head[1] > 25 or head[1] < -25:
        game_over = True 

    # Phase 6 - check for snake biting itself 
    for seg in snake:
        if seg is not head and head[0] == seg[0] and head[1] == seg[1]:
            game_over = True 
            break    

# Phase 4 - Function that checks to see if snake collides with the apple
def check_apple(head):
    global appleCor, apple, growth
    if head[0] == appleCor[0] and head[1] == appleCor[1]:
        #make new randomized coordinates for the apple
        appleCor[0] = random.randint(-24, 24)
        appleCor[1] = random.randint(-24, 24)

        #remove the previous apple 
        stage.remove_sprite(apple)

        #add new apple 
        apple = codesters.Circle(appleCor[0] * 10, appleCor[1] * 10, 10, "red")
        
        #increase the growth of the snake 
        growth += 3

# Phase 3 - Main Game Function
def main():
    #global variables 
    global game_over, snake, growth
    
    #set up game variables
    size = 10
    segs = []
    
    #Add first head to the list of snake positions
    snake.append((0,0))
    seg = snake[0]
    
    #draw first head 
    circle = codesters.Circle(seg[0] * size, seg[1] * size, size, "orange")
    
    # add first head to list of snake sprites 
    segs.append(circle)
    
    # while loop for when users play the game 
    while game_over is False:
        #get head of the snake 
        head = snake[len(snake) - 1]
        
        #calculate and add a new head to the list of snake positions 
        snake_x = head[0] + snakeDx
        snake_y = head[1] + snakeDy
        snake.append((snake_x, snake_y))
        
        # get new head of the snake
        head = snake[len(snake) - 1]
        
        #draw new head 
        circle = codesters.Circle(head[0] * size, head[1] * size, size, "orange")
        
        #add new head to the list of snake sprites 
        segs.append(circle)

        #Phase 4-check to see if snake has eaten the apple
        check_apple(head)

        #Phase 5-check to see if snake has collided with the wall 
        check_state(head)

        #check to see if snake is growing, if so let it grow
        if growth > 0:
            growth -= 1
        #remove tail end of the snake from both lists and form the game screen
        else: 
            snake.pop(0)
            stage.remove_sprite(segs[0])
            segs.pop(0)
        stage.wait(0.1)
    # Phase 5 - display text saying the game is over 
    text = codesters.Text("Game Over", 0, 0, "red")

# Call function
main()