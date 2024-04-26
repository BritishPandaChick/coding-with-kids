obstacles = []

player = codesters.Sprite("person1")
player.set_size(.5)
stage.set_gravity(10)

game_over = False
score = 0
score_text = codesters.Text("Score: 0", 0,150, "grey")

def initialize():
    stage.set_background_color("lightblue")
    stage.disable_all_walls()
    ground = codesters.Rectangle(0, -250, 1000, 100, "red")
    ground.set_gravity_off()

# Phase 3 code
def collision(player, hit_sprite):
    global game_over
    
    player.set_y_speed(0)
    player.set_gravity_off()
    
    if hit_sprite.get_color() is "blue":
        codesters.Text("You Lose!", 0, 0, "red")
        game_over = True
player.event_collision(collision)

# Phase 2 code
def create_obstacles():
    distance = 300
    x = -100
    y = -150
    
    for i in range(5):
        x = x + distance
        new_obstacle = codesters.Rectangle(x, y, 50, 100, "blue")
        new_obstacle.set_gravity_off()
        obstacles.append(new_obstacle)
        
def scroll_world(dx, dy):
    for s in obstacles:
        s.set_x(s.get_x()+dx)
        s.set_y(s.get_y()+dy)

# Phase 4 code 
def jump():
    global player
    player.set_y_speed(10)
    player.set_gravity_on()

def update_score():
    global score
    
    for s in obstacles:
        if s.get_x() < -250:
            score = score + 1
            obstacles.remove(s)
            stage.remove_sprite(s)

initialize()
create_obstacles()

while game_over == False:
    scroll_world(-5, 0)
    stage.event_key("space", jump) # add phase 4
    update_score() # add phase 4
    
    score_text.set_text("Score: " + str(score))
    
    stage.wait(0.05)