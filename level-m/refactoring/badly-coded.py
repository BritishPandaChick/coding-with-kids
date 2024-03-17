t = turtle.Turtle()
t.setposition(0,0)
t.speed(100)
t.penup()

# create square function
def draw_square(size):
    t.pendown()
    for x in range(4):
        t.move_forward(size)
        t.turn_right(90)
    t.penup()

# create pick random color function
def pick_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.color(red, green, blue)

while True:
    t.go_to(random.randint(-230, 230), random.randint(-230, 230))
    t.setheading(0)
    pick_random_color() # add function call
    draw_square(random.randint(10, 50)) # add function call