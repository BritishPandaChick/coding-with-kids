'''
1. Create a list of various words.
2. Find the word which is the longest and print it to the console.
3. Find the word which is the shortest and print it to the console.
'''
words = ["Hi", "Python", "conditionals", "I", "codesters"]
shortest = words[0]
longest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word
    if len(word) > len(longest):
        longest = word
        
print("The shortest word is {}.".format(shortest))
print("The longest word is {}.".format(longest))

'''
Write a function that takes a number and a list of numbers as a parameter.
The program then returns how many numbers in the list are less than the number given.
Challenge #1: Also return a list of all the numbers that are less than the number given.
Challenge #2: Randomly generate a list of numbers to test the program.

What is less than 5 in [8, 8, 2, 3, 2, 3, 0, 0, 6, 0]?
(7, [2, 3, 2, ,3, 0, 0, 0])
'''

import random

def less_than(num, num_list):
    counter = 0
    less_list = []
    for elem in num_list:
        if elem < num:
            counter += 1
            less_list.append(elem)
    return (counter, less_list)
        
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 10))
print(less_than(5, my_list))