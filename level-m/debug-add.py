#this program should modify the numbers as shown and then print out the new values..
#Try to debug the errors and figure out what is happening!
number1 = 10
number2 = 3
number3 = 7
number4 = 0

def debug_add():
    global number3, number4
    number4 = number1 + number2
    number3 = number3 + number4
debug_add()
print(number1) #should be 10
print(number2) #should be 3
print(number3) #should be 20
print(number4) #should be 13