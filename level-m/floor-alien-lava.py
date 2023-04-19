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