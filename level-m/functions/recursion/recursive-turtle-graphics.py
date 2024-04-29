# make the turtle that will be drawing 
turtle = turtle.Turtle()
turtle.shape("classic")
turtle.penup()
turtle.goto(0, 0)
turtle.speed(20)

# draw an equilateral triangle where each side is a given length
def eq_triangle(length):
    turtle.pendown()
    for turn in range(3):
        turtle.forward(length)
        turtle.right(120)
    turtle.penup()
    
# draw triangles inside triangles, with each being smaller than the previous until the triangles have sides smaller than 1
def recursive_triangle(length):
    if length > 1:
        eq_triangle(length)
        recursive_triangle(length - 10)
        
# call the recursive 
recursive_triangle(100)

#draw a square where each side is a given length
def square(length):
    turtle.pendown()
    for turn in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()

# draw squares inside squares, with each being smaller than previous, until the squares have sides smaller than 1 
def recursive_square(length):
    if length > 1:
        square(length)
        recursive_square(length/1.25)

turtle.go_to(0, 125)
recursive_square(100)