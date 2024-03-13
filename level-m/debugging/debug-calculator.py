#This program is a simple calculator that should be able to add, subtract, divide, and multiply
#Currently there are issues with all of these, try to debug the program and get it working, one
#section at a time!

def addition(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result
    
def divide(number1, number2):
    result = number1 / number2
    return result 

def multiply(number1, number2):
    result = number1 * number2
    return result

def calculator():
    calc = codesters.Sprite("person1")
    calc.say("Hello, welcome to your friendly calculator program!")
    stage.wait(2)
    calc.say("You will be asked to enter two numbers and then which operator to apply to them.")
    stage.wait(3)
    calc.say("Have fun!")
    stage.wait(2)
    number1 = int(calc.ask("Please enter the first number"))
    number2 = int(calc.ask("Please enter the second number"))
    operator = calc.ask("Please enter the operator (+, -, /, *)")
    if operator is "+":
        answer = addition(number1, number2)
    elif operator is "-":
        answer = subtract(number1, number2)
    if operator is "/":
        answer = divide(number1, number2)
    else:
        answer = multiply(number1, number2)
    calc.say("The answer is " + str(answer))
calculator()