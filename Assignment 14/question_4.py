print("enter a number separated by comma")
x = input()
l1 = x.split(",")
l2 = [int(i) for i in l1]
print(l2)
print(max(l2))