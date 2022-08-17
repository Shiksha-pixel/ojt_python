'''
Define a function which can print a dictionary where the keys are numbers between 1
and 20 (both included) and the values are square of keys.
Hints: Use dict[key]=value pattern to put entry into a dictionary. 
'''
d=dict()
for x in range(1,21):
    d[x]=x**2
print(d)  