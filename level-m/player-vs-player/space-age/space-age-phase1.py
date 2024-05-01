stage.set_background("scrollingspace")
stage.disable_all_walls()

# set up the sprites
p1_sprite = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
p1 = codesters.Sprite(p1_sprite, -220, 0)
p1.set_size(0.1)
p1.lives = 3

p2_sprite =  "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"
p2 = codesters.Sprite(p2_sprite, 220, 0)
p2.set_size(0.1)
p2.flip_right_left()
p2.lives = 3