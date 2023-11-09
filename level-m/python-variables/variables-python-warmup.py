# create a score variable that is set equal to 0 
score = 0 
print("Score is originally {}".format(score))

# create a function called set_score which takes a number as an input (new value set the score) 
def set_score(new_score):
    score = new_score 
    print("New score should be {}".format(score))
    
# set a score to the value held by the parameter
set_score(100)
print("But the score is still {}".format(score))