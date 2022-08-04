'''
49. Write a program which can map() to make a list whose elements are square ofnumbers
between 1 and 20 (both included).
Hints: Use map() to generate a list. Use lambda to define anonymous functions
'''
li = [i for i in range(1,21)]
evenNumbers = map(lambda x: x**2, li)
print(list(evenNumbers))