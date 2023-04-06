# Create turtle sprite and set it up. Also want to bring the pen up.
t = turtle.Turtle()
t.go_to(0,0)
t.penup()
t.speed(100)

# draw a triangle 
def draw_triangle(x, y, size, color):
    t.go_to(x,y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for x in range(3):
        t.forward(size)
        t.right(120)
    t.penup()

# draw a square
def draw_square(x, y, size, color):
    t.go_to(x,y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.pendown()
    for x in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    
# draw a circle 
def draw_circle(x, y, size, color):
    t.go_to(x,y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for x in range(36):
        t.forward(size)
        t.right(10)
    t.penup()
    
# Call our functions 
draw_triangle(-100, -100, 50, "blue")
draw_square(0, 0, 100, "red")
draw_circle(-150, 150, 10, "green")