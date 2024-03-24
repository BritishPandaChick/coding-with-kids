stage.set_background("space")
stage.disable_all_walls()

still_flying = True # add phase 3
meteors = [] 
ufo = codesters.Sprite("ufo")

def up_key():
    ufo.move_up(20)
    
def down_key():
    ufo.move_down(20)
    
stage.event_key("up", up_key)
stage.event_key("down", down_key)

def create_meteor():
    global meteors
    meteor = codesters.Sprite("meteor1", -300, random.randint(-220, 220))
    meteor.set_size(0.5)
    meteor.set_x_speed(5)
    meteors.append(meteor)
    
# Phase 3 - main game loop
def main():
    while still_flying is True:
        create_meteor()
        stage.wait(2)
        for sprite in meteors:
            if sprite.get_x() > 250:
                stage.remove_sprite(sprite)
                meteors.remove(sprite)
main()