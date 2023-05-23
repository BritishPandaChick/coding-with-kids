#this program should create a list that has numbers from 1 to 10
#Currently it prints a list that has 0, 9, 8, 7, 6, 5, 4, 3, 2, 1
li = []

def debug_list():
    for num in range(1,10):
        li.insert(num, num)
debug_list()
print(li)