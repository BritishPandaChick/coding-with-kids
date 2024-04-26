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

initialize()
create_obstacles()

while game_over == False:
    scroll_world(-5, 0)
    score_text.set_text("Score: " + str(score))
    
    stage.wait(0.05)