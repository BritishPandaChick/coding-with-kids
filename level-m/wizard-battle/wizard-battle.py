import random

#set up background and players 
stage.set_background("castle")
player = codesters.Sprite("wizard", 200, -100)
enemy = codesters.Sprite("evilwitch", -180, -100)

# creates and shoots iceballs 
def shoot_ice():
    iceball = codesters.Circle(player.get_x() - 40, player.get_y() + 70, 30, "lightblue")
    iceball.set_opacity(0.85)
    iceball.set_rotation(random.randint(150, 210))
    iceball.set_speed(2)
    iceball.move_forward(500)
    stage.remove_sprite(iceball)
    
# creates and shoots fireballs 
def shoot_fire():
    fireball = codesters.Sprite("meteor1", enemy.get_x() + 50, enemy.get_y() + 40)
    fireball.set_size(0.4)
    fireball.set_rotation(random.randint(-30, 30))
    fireball.set_speed(2)
    fireball.move_forward(500)
    stage.remove_sprite(fireball)
    
# Event Listeners
stage.event_key("space", shoot_ice)
stage.event_interval(shoot_fire, 2)