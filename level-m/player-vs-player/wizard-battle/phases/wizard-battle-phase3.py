import random

#set up background and players 
stage.set_background("castle")

player = codesters.Sprite("wizard", 200, -100)
player.hp = 10 # add phase 2

# add phase 3
wizard = codesters.Sprite("evilwizard", -220, -40)
wizard.hp = 10
witch = codesters.Sprite("evilwitch", -180, -100) # update enemy to witch variables
witch.hp = 10 # add phase 2 - change enemy to witch in phase 3

# add phase 3 -setup game variables
enemies = [witch, wizard]
can_shoot = True
can_shield = True
play_game = True

# Phase 2 - controls what happens when ice hits computer character 
def ice_hit(sprite, hit_sprite):
    global can_shoot, play_game # add phase 3
    if play_game and (hit_sprite in enemies): # add phase 3
        stage.remove_sprite(sprite)
        can_shoot = True # add phase 3
        hit_sprite.hp -= 1
        hit_sprite.say("I'm hit")
        hit_sprite.wait(1)
        hit_sprite.say("")
        if hit_sprite.hp <= 0 and hit_sprite in enemies: # add phase 3
            enemies.remove(hit_sprite)
        if hit_sprite.hp <= 0:
            codesters.Text("Game Over!", 0, 200, "darkBlue")
            stage.remove_sprite(hit_sprite)

# Phase 2 - controls what happens when fireball hits user character 
def fire_hit(sprite, hit_sprite):
    global can_shield, play_game # add phase 3
    if play_game: # add phase 3
        if hit_sprite.get_color == "white":
            stage.remove_sprite(sprite) # add phase 3
            stage.remove_sprite(hit_sprite) # add phase 3
            can_shield = True # add phase 3
        elif hit_sprite == player: # add phase 3
            stage.remove_sprite(sprite)
            hit_sprite.hp -= 1
            if hit_sprite.hp <= 0:
                play_game = False # add phase 3
                codesters.Text("Game Over!", 0, 200, "darkRed")
                stage.wait(1) # add phase 3
                stage.remove_sprite(hit_sprite)
    
# creates and shoots fireballs 
def shoot_fire():
    if play_game: # add phase 3
        enemy = random.choice(enemies)
        fireball = codesters.Sprite("meteor1", enemy.get_x() + 50, enemy.get_y() + 40)
        fireball.event_collision(fire_hit) # add phase 2
        fireball.set_size(0.4)
        fireball.set_rotation(random.randint(-30, 30))
        fireball.set_speed(2)
        fireball.move_forward(500)
        stage.remove_sprite(fireball)
        
# creates and shoots iceballs 
def shoot_ice():
    global can_shoot
    if can_shoot and play_game:
        iceball = codesters.Curve(130, -30, 180, -60, 160, 10, 130, -130, "lightblue", None) # add phase 5
        iceball.event_collision(ice_hit) # add phase 2
        iceball.set_opacity(0.85)
        iceball.set_rotation(random.randint(150, 210))
        iceball.set_speed(2)
        iceball.move_forward(500)
        stage.remove_sprite(iceball)
        can_shoot = True # add phase 3
        
# Phase 3 - create a shield
def shield():
    global can_shoot, can_shield
    if can_shield and play_game:
        can_shoot = False
        can_shield = False
        shield = codesters.Curve(0, 0, -15, 80, -15, 120, 0, 200, "white", None)
        shield.set_opacity(0.3)
        shield.go_to(player.get_x() - 70, player.get_y())
        stage.wait(2)
        stage.remove_sprite(shield)
        can_shoot = True
        stage.wait(1)
        can_shield = True
        
# Event Listeners
stage.event_key("space", shoot_ice)
stage.event_key("s", shield) # add phase 3
stage.event_interval(shoot_fire, 2)