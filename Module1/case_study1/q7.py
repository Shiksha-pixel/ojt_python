row=int(input("enter no of rows: "))
col=int(input("enter no of cols: "))
mat=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(i*j)
    mat.append(temp)

print(mat)