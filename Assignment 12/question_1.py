num = int(input("enter the number "))
rev_num = 0
while num>0:
    rem = num%10
    rev_num = (rev_num * 10) + rem
    num = num//10
print("reverse of a number: ",rev_num)