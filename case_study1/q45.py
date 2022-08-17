'''
Write a program which can filter even numbers in a list by using filter function. The list
is: [1,2,3,4,5,6,7,8,9,10].
Hints: use filter() to filter some elements in a list. Use lambda to define anonymous
functions.
'''
def even(item):
    if item % 2 == 0:
        return item**2


lst = [i for i in range(1, 11)]
print(list(filter(lambda j: j is not None, list(map(even, lst)))))