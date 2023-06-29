t = turtle.Turtle()
t.penup()
t.speed(100)

def draw_triangle(x, y, size, color):
    t.go_to(x, y)
    t.setheading(60)
    t.pendown()
    t.color(color)
    for x in range(3):
        t.forward(size)
        t.right(120)
    t.penup()
    
def draw_square(x, y, size, color):
    t.go_to(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for x in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    
def draw_circle(x, y, size, color):
    t.go_to(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for x in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    
def draw_circle(x, y, size, color):
    t.go_to(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for x in range(36):
        t.forward(size)
        t.right(10)
    t.penup()
    
def face():
    draw_circle(-120, 110, 10, "black")
    draw_circle(-120, 50, 3, "black")
    draw_circle(120, 110, 10, "black")
    draw_circle(120, 50, 3, "black")
    
    draw_triangle(-25, 0, 50, "red")
    
    draw_square(-35, -80, 70, "red")
    
face()