'''
1. Create a list of 100 random numbers from 1 to 20.
2. Count how many times the number 11 shows in the list.
3. Print the result to the console.
'''
numbers = []
for i in range(100):
    numbers.append(random.randint(1,100))
    
count = 0
for num in numbers:
    if num == 11:
        count += 1
print(count)

'''
Write a function that takes a list as a parameter.
It should return the first and last element of the list.
[1, 2, 3, 4, 5]
(1, 5)
'''
def first_and_last(my_list):
    first = my_list[0]
    last = my_list[-1]
    return(first, last)
print(first_and_last([1, 2, 3, 4, 5]))