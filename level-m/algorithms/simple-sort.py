import random

# create random list of numbers
def create_list():
    nums = []
    for i in range(10):
        nums.append(random.randint(-1000, 1000))
    return nums
    
# swaps two elements in a given list
def swap(lst, i1, i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
    
#sorts a random list of numbers using simple sort 
def simple_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i , len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        swap(lst, minimum, i)

# main function that runs the simple sort
def main():
    rlist = create_list()
    print(rlist)
    simple_sort(rlist)
    print(rlist)
main()
