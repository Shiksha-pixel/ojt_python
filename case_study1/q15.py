'''
15. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
value of a.
Suppose the input is supplied to the program: 9
Then, the output should be: 11106
'''



def function(a):
    d1=a
    d2=10*a+a
    d3=10*d2+a
    d4=10*d3+a
    return d1+d2+d3+d4

a=int(input("enter a number a for function a+aa+aaa+aaaa: "))

print(function(a))