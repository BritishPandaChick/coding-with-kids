alien = codesters.Sprite("alien2", 0, 0)
alien.onPlatform = False 
alien.alive = True
alien.set_size(0.3)

level = 0
stage.set_gravity(10)
platforms = []
stage.disable_ceiling()
min_speed = 1
max_speed = 3
text = codesters.Text("level: 0", -200, 200)
lava = codesters.Rectangle(0, -250, 500, 20, "red")