import math 

stage.set_background_color("grey")
stage.disable_all_walls()

#setup sprites and bases 
base1 = codesters.Circle(-225, -225, 200, "brown")
base2 = codesters.Circle(225, 225, 200, "brown")
base1wall = codesters.Arc(-180, -190, 70, 330, 120, "sienna")
base2wall = codesters.Arc(190, 180, 70, 160, 310, "sienna")
player = codesters.Sprite("robot", -200, -200)
player.set_size(0.5)
computer = codesters.Sprite("enemy", 210, 210)
computer.set_size(0.5)

#setup game variables 
player.lives = 5
computer.lives = 5
game_over = False

#When player clicks, the player throws a snowball at the clicked coordinates
def click():
    throw()
stage.event_click(click)

# calculate vector from player to point licked, vectors are calculated by subtracting the second point by the first point (difference)
def calculate_vector(mouseX, mouseY):
    vector_x = mouseX - player.get_x()
    vector_y = mouseY - player.get_y()
    return [vector_x, vector_y] # return the x and y component of the vector as a list 

#gets the magnitude of a vector; formula here where c is the magnitude: c^2 = a^2 + b^2 => c = sqrt(a^2 + b^2)
def magnitude(vector):
    return math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])

#normalize a vector by dividing by the magnitude 
def divide(vector, number):
    if number == 0:
        return vector
    normX = vector[0] / number #normalize x component 
    normY = vector[1] / number #normalize y component 
    return [normX, normY]

#player throws a snowball towards a clicked point on the stage using vectors and velocity
def throw():
    #actual vector to the clicked point.
    vector = calculate_vector(stage.click_x(), stage.click_y())
    # get the magnitude of the vector so we can normalize the vector 
    mag = magnitude(vector)
    # normalize the vector (remove any current magnitude)
    norm = divide(vector, mag)
    shot = codesters.Circle(player.get_x(), player.get_y(), 7, "white")
    # after we normalize the vector, we multiply by 5 so that the speed is constant and moving in the correct direction.
    x_speed = norm[0] * 5
    y_speed = norm[1] * 5
    shot.set_x_speed(x_speed)
    shot.set_y_speed(y_speed)
# when the player clicks, the player throws a snowball at the clicked coordinates 
stage.event_click(throw)

#create a new enemy shot with random x and y speed (causing the snowballs direction to be randomized)
def enemy_throw():
    c_shot = codesters.Circle(computer.get_x(), computer.get_y(), 7, "black")
    c_shot.set_x_speed(-1 * random.randint(1, 5))
    c_shot.set_y_speed(-1 * random.randint(1, 3))

#collision for both the player and the computer 
def collision(sprite, hit_sprite):
    global game_over
    name = sprite.get_image_name()
    color = hit_sprite.get_color()
    if name is "robot" and color is "black":
        stage.remove_sprite(hit_sprite)
        sprite.say("Ouch!")
        player.lives -= 1
        if player.lives < 1:
            game_over = True
    elif name is "enemy" and color is "white":
        stage.remove_sprite(hit_sprite)
        sprite.say("Ouch!")
        computer.lives -= 1
        if computer.lives < 1:
            game_over = True 
player.event_collision(collision)
computer.event_collision(collision)

#main game function, runs the game
def main():
    while game_over is False:
        enemy_throw()
        stage.wait(2)
    
    if player.lives > 0:
        #sprite = codesters.Text("text", x, y)
        sprite = codesters.Text("Player Wins", 0, 0, "red")
        sprite.set_text_size(50)
    else:
        sprite = codesters.Text("Computer Wins", 0, 0, "red")
        sprite.set_text_size(50)

if __name__ == "__main__":
    main()
