'''
40. Define a function which can generate a list where the values are square of numbers
between 1 and 20 (both included). Then the function needs to print all values exceptthe
first 5 elements in the list.
Hints: Use ** operator to get power of a number. Use range() for loops. Use list.append() to
add values into a list. Use [n1:n2] to slice a list
'''
sqr=[]
for i in range(20):
    sqr.append((i+1)**2)
print(sqr[5:])