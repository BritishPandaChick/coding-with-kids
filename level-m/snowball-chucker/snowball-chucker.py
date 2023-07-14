stage.set_background_color("grey")
stage.disable_all_walls()

#setup sprites and bases 
base1 = codesters.Circle(-225, -225, 200, "brown")
base2 = codesters.Circle(225, 225, 200, "brown")
player = codesters.Sprite("robot", -200, -200)
player.set_size(0.5)
computer = codesters.Sprite("enemy", 210, 210)
computer.set_size(0.5)

#setup game variables 
player.lives = 5
computer.lives = 5
game_over = False

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