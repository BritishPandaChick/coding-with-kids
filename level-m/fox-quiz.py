fox = codesters.Sprite("fox")
stage.set_background("underwater")
score = 0

# first question
guess = fox.ask("What am I?")

if guess is "A fox" or guess is "a fox" or guess is "Fox" or guess is "fox":
    fox.say("Good job I guess")
    score += 2
else:
    fox.say("Nope!")
    score -= 1

stage.wait(3)
fox.say("Your score is: " + str(score))
stage.wait(3)

# second question
guess = fox.ask("where am I?")

if guess is ("underwater") or guess is "the ocean" or guess is "The ocean" or guess is "Underwater" or guess is "the sea" or guess is "The sea" or guess is "sea" or guess is "Sea":
    fox.say("Wow you got one right?!")
    score += 2
else:
    fox.say("How could you miss it? It's a pretty easy question")
    score -= 1
    
stage.wait(4)
fox.say("Your score is: " + str(score))
stage.wait(3)

# second question
stage.set_background("city")

guess = fox.ask("Where am I now?")
if guess is ("a city") or guess is "A city" or guess is "a town" or guess is "A town" or guess is "the city" or guess is "a city" or guess is "city" or guess is "City":
    fox.say("It was a pretty easy question but good job I suppose")
    score += 2
else:
    fox.say("You missed one? How?")
    score -= 1
    
stage.wait(5)
fox.say("Your score is: " + str(score))
fox.say("Good job finishing this quiz, have a picture of a penguin")
sprite = codesters.Sprite("penguin")