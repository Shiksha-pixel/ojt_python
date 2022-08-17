#square rooot using the formula : [(2 * C * D)/H]
ds=input("enter the value of Ds seperated by comma: ").split(',')
print(ds)
c=50
h=30

ans=[]
for d in ds:
    ans.append(str(int((2*c*int(d))/h)))
print(",".join(ans))

