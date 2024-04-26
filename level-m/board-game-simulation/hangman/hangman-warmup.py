# Exercise 1
w = input("Enter a word: ")
a = input("Enter a sentence: ")
if w in s:
    print("yes")
else:
    print("no")
    
# Exercise 2 
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Exercise 3 
x = 0
a = []

while True:
    x = input("Enter a number (done to quit): ")
    if x == "done":
        break
    else:
        a.append(int(x))
        
a.sort()
print(a)

# Exercise 4
a = []

while True:
    x = input("Enter a word (done to quit): ")
    if x == "done":
        break
    else:
        a.append(x)

sentence = " ".join(a)
print(sentence + ".")