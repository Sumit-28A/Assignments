num_1 = int(input("enter the first number "))
num_2 = int(input("enter the second number "))
for e in range(num_1,(num_2)+1):
    if e>1:
        for i in range(2,e):
            if e%i==0:
                break
        else:
            print(e,end=" ")