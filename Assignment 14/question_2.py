print("enter the number ")
x = int(input())
l1 = []
for i in range(1,2*x):
    if i%2!=0:
        l1.append(i)
print(l1)