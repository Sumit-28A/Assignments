print("enter some numbers seprated by comma")
s1 = input()
l1 = s1.split(",")
l2 = [int(i) for i in l1]
print(l2)
print(sum(l2))