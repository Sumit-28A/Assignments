print("enter the coefficent value of x**x ")
a = int(input())
print("enter the coefficent value of x ")
b = int(input())
print("enter the constant value  ")
c = int(input())
d = b**2-4*a*c
if d>0:
    print("roots are real and distinct ")
elif d<0:
    print("roots are imaginary ")
else:
    print("roots are real and equal ")