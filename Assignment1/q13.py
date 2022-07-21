'''
13. Write a program that accepts a sentence and calculate the number of letters anddigits.
Suppose the input is supplied to the program: hello world! 123
Then, the output should be: LETTERS 10

DIGITS 3
'''




sentences=input("enter a sentence")
letters=0
dig=0

for i in sentences:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        dig+=1
print("LETTERS, ",letters)
print("DIGITS ",dig)

