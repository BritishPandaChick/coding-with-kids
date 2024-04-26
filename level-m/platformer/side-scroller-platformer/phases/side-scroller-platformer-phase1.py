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
initialize()