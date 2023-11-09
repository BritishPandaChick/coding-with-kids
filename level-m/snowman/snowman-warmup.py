"""
1. Ask user to input a word and then ask them to input a sentence. 
Check if the word is in the sentence. 
If it is, print yes. If not, print no.
"""

w = input("Enter a word: ")
s = input("Enter a sentence: ")
if w in s:
    print("yes")
else:
    print("no")
    

"""
2. Take the words as a user input until the user enters done.
Join these words together to form a sentence.
Don't forget to include the period at the end.
"""

a = []

while True:
    x = input("Enter a word (done to quit): ")
    if x == "done":
        break
    else:
        a.append(x)
        
sentence = " ".join(a)
print(sentence + ".")