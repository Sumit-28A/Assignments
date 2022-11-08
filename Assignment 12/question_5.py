n = int(input("enter the number "))
while True:
    n+=1
    for e in range(2,n+1):
        if n%e==0:
            break
    else:
        print(n)