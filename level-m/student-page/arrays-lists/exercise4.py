'''
1) Write a function that takes a list as a parameter.
2) It should return two new lists, one of all the even elements and one of all the odd elements.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[(2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
'''
def even_odd_list(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return(even, odd)
print(even_odd_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))