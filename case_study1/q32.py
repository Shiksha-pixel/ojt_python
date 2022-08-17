'''
32. Define a function that can accept an integer number as input and print the "It is an even
number" if the number is even, otherwise print "It is an odd number"
'''
# Python Program to Check If a Number is Odd or Even using If-else Statement

print ("Enter an integer number to check:\n")

x = int (input ())

if (x % 2 == 0):
    print ("The input number is even.\n")
else:
    print ("The input number is odd.\n")