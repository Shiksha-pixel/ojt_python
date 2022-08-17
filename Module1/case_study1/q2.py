'''
Write a program which can compute the factorial of a given numbers. The results should
be printed in a comma-separated sequence on a single line.
'''
def factorial(n):
    if n==1 or n==0:
        return n
    fact=1

    for i in range(2,n+1):
        fact*=i

    return fact

numbers=[]
n=int(input("no fo elements"))
for i in range(n):
    numbers.append(int(input()))

facts=[]
for num in numbers:
    facts.append(str(factorial(num)))

print(','.join(facts))