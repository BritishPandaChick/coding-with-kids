import random

#list of colors 
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#global variables
xspeed = random.randint(-10, 10)
yspeed = random.randint(-10, 10)

#global_balls function - crates all balls for the simulation
def global_balls(num):
    for i in range(num):
        color = random.choice(colors)
        ball = codesters.Circle(0, 0, 25, color)
        ball.go_to(0, random.randint(-250, 250))
        ball.set_x_speed(xspeed)
        ball.set_y_speed(yspeed)
        
#local_balls function
def local_balls(num):
    for i in range(num):
        color = random.choice(colors)
        xspeed = random.randint(-10, 10)
        yspeed = random.randint(-10, 10)
        ball = codesters.Circle(0, 0, 25, color)
        ball.go_to(0, random.randint(-250, 250))
        ball.set_x_speed(xspeed)
        ball.set_y_speed(yspeed)

# main function - controls the creation of the balls 
def main():
    number = int(input("How many balls should I create?"))
    #create number of balls each using a global speed 
    global_balls(number)
    #create a number of balls each with their own speed
    local_balls(number)
    
# run main method 
if __name__ is "__main__":
    main()