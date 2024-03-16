stage.set_background_color("grey")
stage.disable_all_walls()

#set up sprites and bases 
base1 = codesters.Circle(-225, -225, 200, "brown")
base2 = codesters.Circle(225, 225, 200, "brown")
player = codesters.Sprite("robot", -200, -200)
player.set_size(0.5)
computer = codesters.Sprite("enemy", 210, 210)
computer.set_size(0.5)

#setup game variables 
player.lives = 5
computer.lives = 5 
game_over = False