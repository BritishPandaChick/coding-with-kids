stage.set_background("scrollingspace")
stage.disable_all_walls()

# set up the sprites
p1_sprite = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
p1 = codesters.Sprite(p1_sprite, -220, 0)
p1.set_size(0.1)
p1.lives = 3

p2_sprite =  "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"
p2 = codesters.Sprite(p2_sprite, 220, 0)
p2.set_size(0.1)
p2.flip_right_left()
p2.lives = 3

left_firing = False # add phase 3
right_firing = False # add phase 3

# Phase 3 - Lasers and Firing
# fire a laser for player 1
def left_fire():
    global left_firing
    if left_firing is not True:
        left_firing = True
        laser = codesters.TriangleIso(p1.get_x(), p1.get_y(), 5, 10, "blue")
        laser.turn_right(90)
        laser.set_x_speed(10)
        left_firing = False
        
# fire a laser for player 2
def right_fire():
    global right_firing
    if right_firing is not True:
        right_firing = True
        laser = codesters.TriangleIso(p2.get_x(), p2.get_y(), 5, 10, "yellow")
        laser.turn_left(90)
        laser.set_x_speed(-10)
        right_firing = False

# Phase 2 - Player movement
def w_key():
    p1.move_up(10)
stage.event_key("w", w_key)

def s_key():
    p1.move_down(10)
stage.event_key("s", s_key)

# add phase 3
def d_key():
    left_fire()
stage.event_key("d", d_key)

def up_key():
    p2.move_up(10)
stage.event_key("up", up_key)

def down_key():
    p2.move_down(10)
stage.event_key("down", down_key)

# add phase 3
def left_key():
    right_fire()
stage.event_key("left", left_key)