fei = codesters.Sprite("person1")
secret = 3
guess = int(fei.ask("Enter a number from 1 to 10."))

if guess == secret:
    fei.say("Correct!")
elif guess < secret:
    fei.say("Wrong! your guess is lower than my secret number!")
else:
    fei.say("Wrong! your guess is greater than my secret number!")

# Console version
secret = 3
guess = int(input("Enter a number from 1 to 10."))

if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Wrong! your guess is lower than my secret number!")
else:
    print("Wrong! your guess is greater than my secret number!")

# Differentation Activity
secret = 3
guess = int(input("Enter a number from 1 to 10."))

if guess < 1 or guess > 10:
    print("Play again! and enter the number between 1 and 10!")
else:
    if guess == secret:
        print("Correct!")
    elif guess < secret:
        print("Wrong! your guess is lower than my secret number!")
    else:
        print("Wrong! your guess is greater than my secret number!")