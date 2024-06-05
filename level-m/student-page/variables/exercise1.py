'''
1) Set the background image.
2) Make four different sprites appear in each corner of the screen
Hint:  Do not forget to give each sprite a different variable name.
'''
stage.set_background("space")
astronaut1 = codesters.Sprite("astronaut1", -150, 150)
alien1 = codesters.Sprite("alien1", 150, 150)
alien2 = codesters.Sprite("alien2", -150, -150)
alien3 = codesters.Sprite("astronaut2", 150, -150)

'''
1. Create a new project that asks the user for the radius of a circle.
2. Calculate the area contained within that circle using the formula Pi * radius^2.
3. Print out the result of the calculation as shown in the picture.
Challenge: Use string formatting instead of concatenating to the string.
'''
import math

radius = int(input("Enter the radius of a circle:"))
area = math.pi * (radius * radius)
print("The area of the circle is " + str(area))
# challenge with string format: print("The area of the circle is {}".format(area))
