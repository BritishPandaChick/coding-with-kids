stage.set_background("space")
stage.disable_all_walls()

# set up game variables for the game
still_flying = True
meteors = [] 
aliens = [] # add phase 5
aliens_on_screen = 0 # add phase 5
aliens_caught = 0
meteor_speed = 5

# Phase 5 - set score view
score = codesters.Text("Score: " + str(aliens_caught), 0, 255, "orange")

# set up player (ufo) sprite)
ufo = codesters.Sprite("ufo")
ufo.set_size(0.5) # add phase 5
ufo.go_to(200, 0) # add phase 5

# Phase 4 code
def ufo_collision(sprite, hit_sprite):
    global still_flying, aliens_caught, meteor_speed, aliens_on_screen
    # when the player is hit by a meteor, the game ends
    if(hit_sprite.get_image_name() == "meteor1"):
        still_flying = False
        stage.remove_sprite(sprite)
    # add phase 5 - when the player rescues an alien the score goes up
    elif(hit_sprite.get_image_name() == "alien1"):
        aliens_caught += 1
        aliens_on_screen -= 1
        score.set_text("Score: " + str(aliens_caught))
        if aliens_caught % 5 == 0:
            meteor_speed += 1
        stage.remove_sprite(hit_sprite) #add phase 4
ufo.event_collision(ufo_collision)

# set up controls for the spaceship
def up_key():
    ufo.move_up(20)
    
def down_key():
    ufo.move_down(20)
stage.event_key("up", up_key)
stage.event_key("down", down_key)

# create new meteor
def create_meteor():
    global meteors
    meteor = codesters.Sprite("meteor1", -300, random.randint(-220, 220))
    meteor.set_size(0.5)
    meteor.set_x_speed(meteor_speed)
    meteors.append(meteor)

# Phase 5 - add a new alien survivor
def create_alien():
    global aliens_on_screen
    if aliens_on_screen < 2:
        alien = codesters.Sprite("alien1", -300, random.randint(-220, 220))
        alien.set_size(0.25)
        alien.set_x_speed(2)
        aliens_on_screen += 1
        aliens.append(alien)
        
# Phase 3 - main game loop
def main():
    # sets up the meteor and alien sprites to spawn every 2 secons on the left side of the screen
    while still_flying is True:
        create_meteor()
        create_alien() # add phase 5
        stage.wait(2)
        for sprite in meteors:
            if sprite.get_x() > 250:
                stage.remove_sprite(sprite)
                meteors.remove(sprite)
        for sprite in aliens: # add phase 5
            if sprite.get_x() > 250:
                stage.remove_sprite(sprite)
                aliens.remove(sprite)
    for sprite in meteors: # add phase 5
        stage.remove_sprite(sprite)
    for sprite in aliens: # add phase 5
        stage.remove_sprite(sprite)
main()