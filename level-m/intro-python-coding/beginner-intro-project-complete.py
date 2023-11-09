# Exercise 2
sprite = codesters.Sprite("spaceship")
stage.set_background("mars")

# Exercise 8
def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    sprite.set_positions(x, y)
    
stage.event_mouse_move(mouse_move)

# Exercise 9
ufo = codesters.Sprite("ufo")

def interval():
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))

stage.event_interval(interval, 2)

# Exercise 10, 11, 12, 14
hits = 0
hits_text = codesters.Text("Hits: 0", 0, 200)

def collision(sprite, hit_sprite):
    global hits
    sprite.go_to(random.randint(-250, 250), random.randint(-250, 250))
    sprite.say("Ouch", 0.5)
    hits += 1
    hits_text.set_text("Hits: " + str(hits))
    if hits >= 10:
        game_over = codesters.Text("Game Over", 0, 0)
        stage.remove_sprite(sprite)

sprite.event_collision(collision)