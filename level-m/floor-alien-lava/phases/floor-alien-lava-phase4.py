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

# Phase 3 - Scrolling the Platform Sprites
def platform_scrolling(platform, hit_sprite):
    global min_speed, max_speed, level 
    if hit_sprite == lava:
        if alien.alive:
            level += 1
            text.set_text("level: " + str(level))
        min_speed += 1 
        max_speed += 1
        platform.set_x_speed(random.randint(min_speed, max_speed) + random.choice([-1, 1]))
        platform.set_y(500)
        for plat in platforms:
            plat.set_y_speed(plat.get_y_speed() - 0.1) # speed up the game 
        alien.set_y_speed(platforms[0].get_y_speed())

for plat in platforms:
    plat.event_collision(platform_scrolling)

# Phase 4 - Alien jumping and collision
def space_bar():
    if alien.onPlatform:
        alien.set_y_speed(14)
        alien.onPlatform = False 
        alien.set_gravity_on()
        alien.set_x_speed(0)
stage.event_key("space", space_bar) 

def alien_collision(sprite, hit_sprite):
    if hit_sprite == lava:
        alien.alive = False 
        stage.remove_sprite(alien)
    elif sprite.get_y_speed() <= 0:
        sprite.set_y_speed(0)
        sprite.set_gravity_off()
        sprite.set_y_speed(hit_sprite.get_y_speed())
        sprite.set_x_speed(hit_sprite.get_x_speed())
        sprite.onPlatform = True 
alien.event_collision(alien_collision)