#recursive algorithm to calculate the sum of number from 1 to n where n is given by the user.
def recursive_sum(num):
    if num > 1:
        return recursive_sum(num - 1) + num
    return 1
    
# get n from user
n = int(input("Please enter a number for n: "))

# calculate sum from 1 to n recursively
print(recursive_sum(n))