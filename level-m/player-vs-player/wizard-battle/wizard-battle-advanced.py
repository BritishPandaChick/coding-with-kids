import random

#set up background and players 
stage.set_background("castle")

player = codesters.Sprite("wizard", 200, -100)
player.hp = 10

wizard = codesters.Sprite("wizard", 200, -40)
wizard.hp = 10
witch = codesters.Sprite("evilwitch", -180, -170)
witch.hp = 10

# set up global variables 
enemies = [witch, wizard]
can_shoot = True 
can_shield = True
play_game = True 

# controls what happens when ice hits computer character
def ice_hit(sprite, hit_sprite):
    global can_shoot, play_game
    if play_game and (hit_sprite in enemies):
        stage.remove_sprite(sprite)
        can_shoot = True
        hit_sprite.hp -= 1
        hit_sprite.say("I'm hit")
        hit_sprite.wait(1)
        hit_sprite.say("")
        if hit_sprite.hp <= 0 and hit_sprite in enemies:
            enemies.remove(hit_sprite)
            if len(enemies) == 0:
                play_game = False 
                codesters.Text("Game Over!", 0, 200, "darkbBlue")
            stage.remove_sprite(hit_sprite)

# controls what happens when fireball hits user character 
def fire_hit(sprite, hit_sprite):
    global can_shield, play_game
    if play_game:
        if hit_sprite.get_color() == "white":
            stage.remove_sprite(sprite)
            stage.remove_sprite(hit_sprite)
            can_shield = True
        elif hit_sprite == player:
            stage.remove_sprite(sprite)
            hit_sprite.hp -= 1
            if hit_sprite.hp <= 0:
                play_game = False
                codesters.Text("Game Over!", 0, 200, "darkRed")
                stage.wait(1)
                stage.remove_sprite(hit_sprite)

# creates and shoots iceballs 
def shoot_ice():
    global can_shoot 
    if can_shoot and play_game:
        can_shoot = False 
        iceball = codesters.Curve(130, -30, 180, -60, 160, 10, 130, -30, "lightBlue", None)
        iceball.event_collision(ice_hit)
        iceball.set_opacity(0.85)
        iceball.set_rotation(random.randint(150, 210))
        iceball.set_speed(2)
        iceball.move_forward(500)
        stage.remove_sprite(iceball)
        can_shoot = True
    
# creates and shoots fireballs 
def shoot_fire():
    if play_game:
        enemy = random.choice(enemies)
        fireball = codesters.Sprite("meteor1", enemy.get_x() + 50, enemy.get_y() + 40)
        fireball.event_collision(fire_hit)
        fireball.set_size(0.4)
        fireball.set_rotation(random.randint(-30, 30))
        fireball.set_speed(2)
        fireball.move_forward(500)
        stage.remove_sprite(fireball)

# create a shield 
def shield():
    global can_shoot, can_shield 
    if can_shield and play_game:
        can_shoot = False 
        can_shield = False 
        shield = codesters.Curve(0, 0, -15, 80, -15, 120, 0, 200, "white", None)
        shield.get_opacity(0.3)
        shield.go_to(player.get_x() - 70, player.get_y())
        stage.wait(2)
        stage.remove_sprite(shield)
        can_shoot = True 
        stage.wait(1)
        can_shield = True
    
# Event Listeners
stage.event_key("space", shoot_ice)
stage.event_key("s", shield)
stage.event_interval(shoot_fire, 2)