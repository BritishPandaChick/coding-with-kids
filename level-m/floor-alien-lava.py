# Phase 1 - Setup 
alien = codesters.Sprite("alien2", 0, 0)
alien.onPlatform = False # is the alien on a platform?
alien.alive = True # is the alien still alive? 
alien.set_size(0.3) 

level = 0 
stage.set_gravity(10)
platforms = []
stage.disable_ceiling() 
min_speed = 1 # platform minimum x speed 
max_speed = 3 # platform minimum x speed 
text = codesters.Text("level: 0", -200, 200) 
lava = codesters.Rectangle(0, -250, 500, 20, "red")

# Phase 2 - Making platform sprites 
def build_platforms():
    plat_y = -220
    for i in range(0,4):
        plat = codesters.Rectangle(0, plat_y, 100, 20, "blue")
        plat.set_x_speed(random.randint(min_speed, max_speed) * random.choice([-1, 1]))
        plat.set_gravity_off()
        plat.set_y_speed(-0.3)
        platforms.append(plat)
        plat_y += 175
build_platforms()