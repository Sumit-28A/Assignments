from calendar import c


print("enter two words :")
a,b = input(),input()
if a > b:
    a,b = b,a
    print(a,b)
else:
    print(a,b)