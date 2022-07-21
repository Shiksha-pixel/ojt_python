str1= input("enter input string: ").split(" ")
str1.sort()
stack=[]
for i in range(len(str1)):
    if i and str1[i]==str1[i-1]:
        continue
    stack.append(str1[i])

print(" ".join(stack))
