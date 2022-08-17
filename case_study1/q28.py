'''
Define a function that can receive two integral numbers in string form and compute
their sum and then print it in console.
Hints: Use int() to convert a string to integer.
'''

def calculateSum (a,b):
	s = int(a) + int(b)
	return s 

# Main code 
# take two integral numbers as strings
num1 = "10"
num2 = "20"

# calculate sum
sum = calculateSum (num1, num2)

# print sum
print "Sum = ", sum