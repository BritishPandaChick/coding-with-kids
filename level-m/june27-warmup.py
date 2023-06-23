# Create a sprite
player = codesters.Sprite("purpleguy", -100, 100)

# key events 
# function to run when the left key is pressed
def left_key():
    player.move_right(20)
stage.event_key("left", left_key)

# function to run when the right key is pressed
def right_key():
    player.move_right(20)
stage.event_key("right", right_key)

# function to run when the up key is pressed
def up_key():
    player.move_up(20)
stage.event_key("left", up_key)

# function to run when the left key is pressed
def down_key():
    player.move_down(20)
stage.event_key("left", down_key)

# create other sprites to collide with 
person = codesters.Sprite("person1", 120, 100)
cat = codesters.Sprite("blackcat", 150, -160)
superhero = codesters.Sprite("superhero2", -120, -160)

# collision events 
def player_collision(myself, other_sprite):
    image = other_sprite.get_image_name() 
    if image is "person1":
        myself.say("Hi there! Nice to meet you!")
        stage.wait(1)
        myself.say("")
        other_sprite.say("Hi there purple guy, nice to meet you!")
    elif image is "blackcat":
        myself.say("Hey kitty!")
        stage.wait(1)
        myself.say("")
        cat.say("Meow!")
    else:
        myself.say("Whoa! A superhero, so cool!")
        stage.wait(1)
        myself.say("")
        superhero.say("Hi there citizen! Have a lovely day!")
player.event_collision(player_collision)

# mouse or click events 
def click(sprite):
    sprite.say("Hello, my name is Emily!")
person.event_click(click)

def click(sprite):
    sprite.say("Meow! Meow!")
cat.event_click(click)

def click(sprite):
    sprite.say("I'm a superhero!")
superhero.event_click(click)