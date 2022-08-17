'''
Define a function which can compute the sum of twonumbers.
Hints: Define a function with two numbers as arguments. You can compute the sum in the
function and return the value.
'''

from binascii import a2b_base64


def add(a1,a2):
    return (a1+a2)

ans=input("enter two number to calculate the sum separated by comma ")

ans=ans.split()

print(add(int(ans[0]),int(ans[1])))
