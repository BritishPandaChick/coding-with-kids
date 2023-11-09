# 1. Create a variable "x" with a value of 10
x = 10

# 2. Get a sprite and a background
sprite = codesters.Sprite("spaceship")
stage.set_background("mars")

# 3. Make the sprite move 3 different positions. Extra challenge is to make the postions random.
sprite.go_to(-100, 50)
sprite.go_to(100, -50)
sprite.got_to(0, 0)

"""Advanced
for in range(3):
    sprite.go_to(random.randint(-250, 250), random.randint(-250, 250))
    stage.wait(1)
"""

# 4. Print "Hello World!" to the console.
print("Hello World!")

# 5. Print your variable "x" to the console.
print(x)

# 6. Print the x and y coordinates of the sprite in the console.
print(sprite.get_x(), sprite.get_y())

# 7. Print out the numbers 1 through 10 to the console. Hint: Use a loop.
for i in range(1, 11):
    print i

# 8. Make the sprite always go to the pointer.
def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    sprite.set_positions(x, y)
    
stage.event_mouse_move(mouse_move)

#9. Add another sprite that goes to a new random position every 2 second. Every time it moves it should print out its new location in the console.
ufo = codesters.Sprite("ufo")

def interval():
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))

stage.event_interval(interval, 2)

# 10.Add in the functionality to check if the sprites hit one another. If they hit each other, one of them should say "ouch"
def collision(sprite, hit_sprite):
    sprite.say("Ouch", 0.5)

sprite.event_collision(collision)

# 11.Add in a variable that keeps track of how m any times the sprites have hit each other.
hits = 0

def collision(sprite, hit_sprite):
    global hits
    sprite.say("Ouch", 0.5)
    hits += 1
    
# 12.If the sprites have hit each other 10 times, then they should stop moving and text saying game_over should appear on the screen.
def collision(sprite, hit_sprite):
    global hits
    sprite.say("Ouch", 0.5)
    hits += 1
    if hits >= 10:
        game_over = codesters.Text("Game Over", 0, 0)
        
# 13.Get a number input from the user and print it out to the console with the text "Number: ".
num = int(input("Enter a number: "))
print("Number: " + str(num))

# 14.Add in a display so that there is always text on the screen displaying the number of times the sprites have hit one another.
hits = 0 

def collision(sprite, hit_sprite):
    global hits
    sprite.go_to(random.randint(-250, 250), random.randint(-250, 250))
    sprite.say("Ouch", 0.5)
    hits += 1
    hits_text.set_text("Hits: " + str(hits))
    if hits >= 10:
        game_over = codesters.Text("Game Over", 0, 0)
        stage.remove_sprite(sprite)

# 15.Get a number input from the user and check if is even or odd. If is even print out "even number". Otherwise print out "odd number".
num= int(input("Enter a number: "))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")