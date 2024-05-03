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

# Phase 4 - Player Collisions
def left_collision(sprite, hit_sprite):
    if hit_sprite.get_color() is "yellow":
        p1.lives -= 1
        stage.remove_sprite(hit_sprite)
p1.event_collision(left_collision)

def right_collision(sprite, hit_sprite):
    if hit_sprite.get_color() is "blue":
        p2.lives -= 1
        stage.remove_sprite(hit_sprite)
p2.event_collision(right_collision)

# Phase 5 - End game and while loop
def game():
    display = codesters.Text("Destroy your opponent!", 0, 220, "red")
    while p1.lives > 0 and p2.lives > 0:
        stage.wait(0.0001)
    if p1.lives > 0:
        display = codesters.Text("Sharkship (Player 2) wins!", 0, 220, "red")
    else:
        display = codesters.Text("Dinoship (Player 1) wins!", 0, 220, "red")
    display.go_to(0, 0)
    stage.remove_sprite(p1)
    stage.remove_sprite(p2)
game()
