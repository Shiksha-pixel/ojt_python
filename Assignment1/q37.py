'''
Define a function which can generate and print a list where the values are squareof
numbers between 1 and 20 (both included).
Hints: Use ** operator to get power of a number. Use range() for loops. Use list.append() to
add values into a list.

'''
sqr=[]

for i in range(20):
    sqr.append((i+1)**2)

for i,val in enumerate(sqr):
    print(i+1,val)