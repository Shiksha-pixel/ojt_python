'''
Write a program which can map() to make a list whose elements are square ofelements
in [1,2,3,4,5,6,7,8,9,10].
Hints: Use map() to generate a list. Use lambda to define anonymous functions.

'''
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
#print(squaredNumbers)
print(list(squaredNumbers))