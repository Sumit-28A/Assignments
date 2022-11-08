print("enter some number seprated by comma")
s1 = input()
l1 = s1.split(',')
l2 = []
for e in l1:
    l2.append(eval(e))
print(l2)
print(min(l2))