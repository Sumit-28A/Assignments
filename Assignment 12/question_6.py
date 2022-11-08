n = int(input(" enter the number "))
count=0
x=2
while count<n:
    for i in range(2,x):                      #range(2,10)
        if x%i==0:
             break
    else:
        print(x,end=" ")
        count+=1
    x+=1