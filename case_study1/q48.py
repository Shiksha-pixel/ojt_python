'''
Write a program which can filter() to make a list whose elements are evennumber
between 1 and 20 (both included).
Hints: Use filter() to filter elements of a list. Use lambda to define anonymous functions.
'''
from Assignment1.q45 import even


evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)