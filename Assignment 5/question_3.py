"""
a=6
b=7
temp=a
a=b
b=temp
print(a,b)

"""

num_1 = int(input(" enter a number_1 "))
num_2 = int(input(" enter a number_2 "))

num_1,num_2 = num_2,num_1

print("new value of num_1 ",num_1)
print("new value of num_2 ",num_2)
