# Phase 1 - Setup 
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

# Phase 2 - Making platform sprites 
def build_platforms():
    plat_y = -220
    for i in range(0,4):
        plat = codesters.Rectangle(0, plat_y, 100, 20, "blue")
        plat.set_x_speed(random.randint(min_speed, max_speed) * random.choice([-1, 1]))
        plat.set_gravity_off()
        plat.set_y_speed(-0.3)
        # property to determine if alien is riding this platform - bonus 
        plat.alien_riding = False # add phase 5
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
            # make alien fall if it is riding the platform - phase 5
            if platform.alien_riding: # add phase 5
                alien.onPlatform = False # add phase 5
                alien.set_gravity_on() # add phase 5
                alien.set_x_speed(0) # add phase 5
        else: # add phase 5
            # remove platform once game is over - phase 5
            stage.remove_sprite(platform) # add phase 5
        platform.set_width(platform.get_width() * 0.9) # add phase 5
        min_speed += 1 
        max_speed += 1
        platform.set_x_speed(random.randint(min_speed, max_speed) + random.choice([-1, 1]))
        platform.set_y(500)
        for plat in platforms:
            plat.set_y_speed(plat.get_y_speed() - 0.1) 
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

# Phase 5 - horizontal movements 
def right_arrow():
    alien.set_x_speed(alien.get_x_speed() + 1)
stage.event_key("right", right_arrow)

def left_arrow():
    alien.set_x_speed(alien.get_x_speed() - 1)
stage.event_key("left", left_arrow)

# check if the alien has fallen off of the platform by moving left or right 
def interval():
    for plat in platforms:
        if plat.alien_riding and abs(plat.get_x()-alien.get_x()) > (plat.get_width()/2):
            alien.onPlatform = False
            alien.set_gravity_on()
            alien.set_x_speed(0)
            plat.alien_riding = False 
stage.event_interval(interval, .01)
