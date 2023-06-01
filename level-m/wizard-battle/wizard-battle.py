import random

#set up background and players 
stage.set_background("castle")
player = codesters.Sprite("wizard", 200, -100)
player.hp = 10
enemy = codesters.Sprite("evilwitch", -180, -100)
enemy.hp = 10

# controls what happens when ice hits computer character
def ice_hit(sprite, hit_sprite):
    if hit_sprite == enemy and hit_sprite.get_image_name() == "evilwitch":
        stage.remove_sprite(sprite)
        hit_sprite.hp -= 1
        hit_sprite.say("I'm hit")
        hit_sprite.wait(1)
        hit_sprite.say("")
        if hit_sprite.hp <= 0:
            codesters.Text("Game Over!", 0, 200, "darkbBlue")
            stage.remove_sprite(hit_sprite)

# controls what happens when fireball hits user character 
def fire_hit(sprite, hit_sprite):
    if hit_sprite == player:
        stage.remove_sprite(sprite)
        hit_sprite.hp -= 1
        if hit_sprite.hp <= 0:
            codesters.Text("Game Over!", 0, 200, "darkRed")
            stage.remove_sprite(hit_sprite)

# creates and shoots iceballs 
def shoot_ice():
    iceball = codesters.Circle(player.get_x() - 40, player.get_y() + 70, 30, "lightblue")
    iceball.event_collision(ice_hit)
    iceball.set_opacity(0.85)
    iceball.set_rotation(random.randint(150, 210))
    iceball.set_speed(2)
    iceball.move_forward(500)
    stage.remove_sprite(iceball)
    
# creates and shoots fireballs 
def shoot_fire():
    fireball = codesters.Sprite("meteor1", enemy.get_x() + 50, enemy.get_y() + 40)
    fireball.event_collision(fire_hit)
    fireball.set_size(0.4)
    fireball.set_rotation(random.randint(-30, 30))
    fireball.set_speed(2)
    fireball.move_forward(500)
    stage.remove_sprite(fireball)
    
# Event Listeners
stage.event_key("space", shoot_ice)
stage.event_interval(shoot_fire, 2)