'''
Write a program that accepts a sentence and calculate the number of upper caseletters
and lower case letters.
Suppose the input is supplied to the program: Hello world!
Then, the output should be: UPPER CASE 1
LOWER CASE 9
'''

sent=input("enter a sentence with upper and lower case letters to count: ")
low=0
up=0
for i in sent:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1

print("UPPER CASE ",up)
print("LOWER CASE ",low)