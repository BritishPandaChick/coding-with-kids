#This is a program that should print You are great at debugging!
#Currently it prints You ar grea still at debu

str1 = "You are a person"
str2 = "I am great"
str3 = "Are we still at debugging!?"

#the [0:6] means that it is only taking from the 1st letter (index 0) to the 7th letter (index 6) of that string
def debug_string():
    theString = str1[0:7]
    theString += str2[5:10]
    theString += str3[12:26]
    print(theString)
debug_string()