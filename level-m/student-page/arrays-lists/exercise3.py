'''
1. Create a sprite that will ask for an x and y position, and glide to that position.
2. Create two lists (xPosition and yPosition) to record locations.
3. Now change your code so that it records the x and y positions into your lists(and doesn't move).
4. Add code to get your sprite to follow the path of x and y positions you have recorded when you want it to begin.
Challenge: Use one list to store both the x and y positions.
'''
sprite = codesters.Sprite('person1')
xpos = []
ypos = []
answer = 'no'

while answer != 'yes':
    x = int(sprite.ask("What x position should I go to next?"))
    y = int(sprite.ask("What y position should I go to next?"))
    xpos.append(x)
    ypos.append(y)
    answer = (sprite.ask("Should I start my path? (Yes or No)"))
    
for i in range(len(xpos)):
    sprite.glide_to(xpos[i], ypos[i])

# Challenge solution
sprite = codesters.Sprite('person1')
positions = []
answer = 'no'

while answer != 'yes':
    x = int(sprite.ask("What x position should I go to next?"))
    y = int(sprite.ask("What y position should I go to next?"))
    positions.append([x, y])
    answer = (sprite.ask("Should I start my path? (Yes or No)"))
    
for positions in positions:
    sprite.glide_to(position[0], position[1])

'''
1) Create two lists.
2) Loop through the list and create a new list that only contains the elements found in both lists.
[1,2, 3, 4, 5]
[2, 4, 6, 8, 10]
[2, 4]
'''
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
new_list = []

for num in list1:
    if num in list2:
        new_list.append(num)
        print(new_list)