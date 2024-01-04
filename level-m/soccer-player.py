def set_stage():
    """ Sets up the stage for the game """
    stage.set_background("soccerfield")
    stage.disable_floor()
    
def add_player():
    """ add a player to the stage for the user to control """
    player = codesters.Sprite("player1")
    player.go_to(0, -155)
    return player 
    
def add_ball(speed):
    """ add a ball to the stage and set its attributes """
    ball = codesters.Sprite("soccerball")
    ball.set_y_speed(speed)
    
def head_ball(sprite, hit_sprite):
    """ Detects collisions between the player and the ball """
    my_var = hit_sprite.get_y_speed()
    hit_sprite.set_y_speed(-my_var + 1)
    
    my_var = hit_sprite.get_x_speed()
    hit_sprite.set_x_speed(my_var + 1)

def move_left(sprite):
    """ moves the player left """
    sprite.move_left(50)
    
def move_right(sprite):
    """ moves the player right """ 
    sprite.move_right(50)
    
def main():
    """ sets up the program and calls other functions """
    set_stage()
    player = add_player()
    add_ball(-10)
    player.event_collision(head_ball)
    
    player.event_key("left", move_left)
    player.event_key("right", move_right)
    
main()