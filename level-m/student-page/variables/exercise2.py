'''
1) Create a list of different sprite images.
2) Randomly select images and spawn these sprites in random positions.
3) Do this until you have created 10 random sprites
Hint:  You might want to use a loop.
'''
import random
sprite_images = ["football", "soccerball", "basketball", "baseball", "baseballbat"]
for i in range(10):
    sprite_image = random.choice(sprite_images)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    sprite = codesters.Sprite(sprite_image, x, y)
    
'''
1. Create a new project that asks the user for an integer and store that into a variable named n.
2. Calculate the result of that n plus itself squared plus itself cubed.
3. Print the result as shown in the image attached. Challenges:
1) String formatting instead of concatenating to a string.
2) Allow the user to enter the number of powers of n to sum (instead of n^3, allow them to do n^x where they are asked for x).

Please enter a integer (whole number): 5
The result is: 155
'''
n = int(input("Please enter an integer (whole number):"))
result = n + n * n + n * n * n
print("The result is: " + str(result))

# string formatting challenge: "The result is: {}".format(result)
# choose number of powers: 
'''
for i in range(int(input("Enter the number of powers of n to sum"))):
    product = 1
    for j in range(i):
        product *= n
    result += product
'''