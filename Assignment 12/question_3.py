num = 100
for e in range(2,num):
    if e>1:
        for i in range(2,e):
            if e%i==0:
                break
        else:
            print(e,end=" ")