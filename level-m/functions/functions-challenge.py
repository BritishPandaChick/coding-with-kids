# codester based version of challenge activity
def triple(num):
    return num*3

number = stage.ask("Enter a number: ", 0, 0)
answer = triple(int(number))
codesters.Text("The triple of " + str(number) + " is " + str(answer))

# console version of challenge activity
def triple(num):
    return num*3

number = int(input("Enter a number: "))
answer = triple(number)
print("The triple of " + str(number) + " is " + str(answer))