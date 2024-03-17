#this code continues asking for values and then adds, subtracts, multiplies or divides
# them and displays the result

#takes an operator (represented by a number) and 2 numbers, and performs that operation

# add operation function
def operation(num1, operator, num2):
    if operator == "1":
        return num1 + num2
    elif operator == "2":
        return num1 - num2
    elif operator == "3":
        return num1 * num2
    elif operator == "4":
        return num1 / num2

# add main function
def main():
    sprite = codesters.Sprite("person2")
    answer = 0

    while answer is not "stop":
        number1 = sprite.ask("Please enter a number.")
        answer = sprite.ask("Please a 2nd number.")
        operator = sprite.ask("Do you want to (1) add, (2) subtract, (3) multiply, or (4) divide to/from the result?")
        if operator not in ["1", "2", "3", "4"]:
            sprite.say("That is not a valid response. Please try again.")
            stage.wait(2)
        else:
            result = operation(int(number1), operator, int(answer))
            sprite.say("Result is now: {}".format(result))
            stage.wait(2)
        answer = sprite.ask("Continue or Stop?").lower()
main()
