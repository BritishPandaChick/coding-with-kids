# Demo Activity
a = 10
b = 12

if a > 0 and b > 0:
    print("The numbers are greater than 0")
elif a > 0 or b > 0:
    print("One of the numbers is greater than 0")
else:
    print("No number is greater than 0")

# nested conditionals 
# Example 1
number = int(input("Enter a number: "))

if number > 100:
    print("Number is 50 or greater than 100.")
else:
    if number >= 50:
        print("Number is 50 or greater than 50!")
    elif number >= 30:
        print("Number is 30 or greater than 30!")
    else:
        print("Number is less than 30")

# Example 2
number = int(input("Enter a number: "))

if number < 100:
    if number >= 50:
        print("Number is 50 or greater than 50!")
    elif number >= 30:
        print("Number is 30 or greater than 30!")
    else:
        print("Number is less than 30")
else:
    print("Number is greater than 100.")