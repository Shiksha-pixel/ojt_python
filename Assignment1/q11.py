'''
11. Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.
'''
bin_nums=input("enter binary number comma seperated: ").split(',')
res=[]

for bins in bin_nums:
    x=int(bins,2)
    if x%5==0:
        res.append(bins)

print(",".join(res))
