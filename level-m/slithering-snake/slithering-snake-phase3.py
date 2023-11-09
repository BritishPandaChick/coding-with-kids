#Phase 1 Code
snake = []
snakeDx = 0
snakeDy = -1
game_over = False
background = stage.set_background_color("green")

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

# Phase 3
def main():
    #global variables 
    global game_over, snake
    
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
    
    #main game loop 
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
        
        #remove tail end of the snake from both lists and form the game screen
        snake.pop(0)
        stage.remove_sprite(segs[0])
        segs.pop(0)
        stage.wait(0.1)
        
# Call function
main()
