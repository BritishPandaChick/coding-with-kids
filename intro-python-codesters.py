print("One")
print("Two")
print("Three")
print("Four")

stage.set_background("winter")
kitten = codesters.Sprite("kitten", -90, -30)
cat = codesters.sprite("cat", 10, 250)
kitten.say("I am a kitten!")
stage.wait(2)

# Exercise 1
x = 10 

# Exercise 2
sprite = codesters.Sprite("spaceship")
stage.set_background("mars")

# Exercise 3
sprite.go_to(-100, 50)
sprite.go_to(100, -50)
sprite.go_to(0, 0)

# Exercise 4
print("Hello World")

# Exercise 5 
print(x)

# Exercise 6
prin(sprite.get_x(), sprite.get_y())

# Exercise 7
for i in range(1, 11):
    print i 

# Exercise 8
def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y() 
    sprite.set_position(x, y)
stage.event_mouse_move(mouse_move)

# Exercise 9
ufo = codesters.Sprite("ufo")

def interval():
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))
stage.event_interval(interval, 2)

# Exercise 10 
# Exercise 11 = add variable to track how many hits 
hits = 0
# Exercise 14
hits_text = codesters.Text("Hits: 0", 0, 200)
def collision(sprite, hit_sprite):
    global hits
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))
    sprite.say("Ouch", 0.5)
    hits += 1 # Exercise 11
    hits_text.set_text("Hits: " + str(hits))
    #Exercise 12
    if hits >= 10:
        game_over = codesters.Text("Game Over", 0, 0)
        stage.remove_sprite(sprite)
    
sprite.event_collision(collision)

# Exercise 13 
num = int(input("Enter a number: ")) 
    #Exercise 15 
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
print("Number: " + str(num))