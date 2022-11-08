num = int(input(" enter the number "))
li = []
while num>0:
    rem = num % 2
    li.append(rem)
    num = num//2
print(li)