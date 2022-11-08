"""
num_1 = int(input("enter first number "))
num_2 = int(input("enter second number "))
num_3 = int(input("enter third number "))

if num_1 > num_2 and num_1 > num_3:
    print("first number is greater ")
elif num_2 > num_3 and num_2 > num_1:
    print("second number is greater ")
else:
    print("third number is greater ")
"""
print("enter three number ")
a,b,c = int(input()),int(input()),int(input())
print((a if a>c else c) if a>b else (b if b>c else c))