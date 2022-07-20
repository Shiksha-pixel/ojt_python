#4. 
'''
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number.
'''
nums=input("type in numbers seperated by a comma: ")

numbers=nums.split(',')

num_tuple=tuple(numbers)
print(num_tuple)
print(numbers)