import random
#create a randomly generated list of numbers.
def create_list():
    nums = []
    for i in range(10):
        nums.append(random.randint(-1000, 1000))
    return nums

#merges the right and left lists together and places their elements into the original list in sorted order.
def merge(original, left, right):
    i = 0
    j = 0
    k = 0
    #while both of the lists have elements left, place them in sorted order into the original list.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            original[k] = left[i]
            i += 1
        else:
            original[k] = right[j]
            j += 1
        k += 1
    #if i < len(left) then there are still elements in left that have not been sorted into the original.
    while i < len(left):
        original[k] = left[i]
        i += 1
        k += 1
    #if j < len(right) then there are still elements in right that have not been sorted into the original.
    while j < len(right):
        original[k] = right[j]
        j += 1
        k += 1
        
#splits the list into 2 halves, then splits each half in half. Continue until only 1 element remains in each half list.
def split(alist):
    if(len(alist) > 1):
        #find middle of list.
        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]
        #split apart the halves
        split(left)
        split(right)
        #merge the halves back together
        merge(alist, left, right)

def merge_sort(a):
    split(a)

def main():
    rlist = create_list()
    print(rlist)
    merge_sort(rlist)
    print(rlist)

main()