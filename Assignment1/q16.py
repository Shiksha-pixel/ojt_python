'''
Use a list comprehension to square each odd number in a list. The list is input by a
sequence of comma-separated numbers.
Suppose the input is supplied to the program: 1,2,3,4,5,6,7,8,9
Then, the output should be: 1, 3, 5, 7, 9
'''
l1=list(map(int,input("enter comma separated numbers: ").split(",")))
print("l1",l1)
res=[]
for i in l1:
    if i%2==1:
        res.append(str(i**2))

print(",".join(res))