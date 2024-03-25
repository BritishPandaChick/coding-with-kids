stage.set_background("space")
stage.disable_all_walls()

# set up variables for the game
still_flying = True # add phase 3
meteors = [] 
aliens = [] # add phase 5
aliens_caught = 0 # add phase 5

# set up player (ufo) sprite
ufo = codesters.Sprite("ufo")
ufo.set_size(0.5)
ufo.go_to(200, 0)

# Phase 4 code
def ufo_collision(sprite, hit_sprite):
    global still_flying, aliens_caught # add aliens_caught phase 5
    if(hit_sprite.get_image_name() == "meteor1"):
        still_flying = False
        stage.remove_sprite(sprite)
    # when the player rescues an alien, the score goes up - add phase 5
    elif(hit_sprite.get_image_name() == "alien1"):
        aliens_caught += 1
        stage.remove_sprite(hit_sprite)
ufo.event_collision(ufo_collision)

# set up controls for spaceship
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
    meteor.set_x_speed(5)
    meteors.append(meteor)
    
# Phase 5 - create new alien survivor
def create_alien():
    global aliens
    alien = codesters.Sprite("alien1", -300, random.randint(-220, 220))
    alien.set_size(0.25)
    alien.set_x_speed(2)
    aliens.append(alien)
    
# Phase 3 - main game loop
def main():
    # set up meteor and alien sprites to spawn every 2 seconds on the left side of the screen
    while still_flying is True:
        create_meteor()
        create_alien() # add phase 5
        stage.wait(2)
        for sprite in meteors:
            if sprite.get_x() > 250:
                stage.remove_sprite(sprite)
                meteors.remove(sprite)
        for sprite in aliens:
            if sprite.get_x() > 250:
                stage.remove_sprite(sprite)
                aliens.remove(sprite)
main()
