n = int(input("enter the number "))
sum=0
while n>0:
    n1 = n % 10
    sum = sum + n1
    n = n //10
print(sum)