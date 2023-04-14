#global variables 
score = 0 
sprite_list = []
display = codesters.Text("Score:", 0, 200, "red")

#on click function for the robot sprites
def click(sprite):
    global score
    score += sprite.points
    display.set_text("Score: {}".format(score))
    sprite.set_x(random.randint(-220, 220))
    sprite.set_y(random.randint(-220, 220))
    
#create the 4 sprites 
def sprite_creation():
    #create 4 robot sprites randomly distributed across the screen 
    for num in range(4):
        sprite = codesters.Sprite("robot", random.randint(-220, 220), random.randint(-220, 220))
        # num starts at 0. Need to up it by 1 for the points each sprite gives
        sprite.points = num + 1
        # add the on click event to the sprites
        sprite.event_click(click)
        # add the sprites to the list of sprites 
        sprite_list.append(sprite)
        
def game():
    #create original sprites 
    sprite_creation()
    #game is over when the score gets above 25 
    while score < 25:
        #for each loop moving each of the sprites every 2 seconds 
        for sprite in sprite_list:
            sprite.set_x(random.randint(-220, 220))
            sprite.set_y(random.randint(-220, 220))
        stage.wait(2)
            