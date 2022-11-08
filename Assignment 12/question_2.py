import math 
  
num = int(input("enter the number "))
if num<2:
    print("not a prime number")
else:
    for e in range(2,int(math.sqrt(num))):
        if num%e==0:
            print("not a prime number")
            break
    else:
        print("prime number")