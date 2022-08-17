'''
17. Write a program that computes the net amount of a bank account based atransaction
log from console input. The transaction log format is shown asfollowing:
D 100
W 200
--D means deposit while W means withdrawal.
Suppose the input is supplied to the program:
D 300

D 300
W 200
D 100
'''
from this import s


tran=input("enter transation").split("/n")

res=0

for t in tran:
    t=t.split()
    if t[0]=="D":
        res+=int(t[1])
    else:
        res-=int(t[1])
print(res)

