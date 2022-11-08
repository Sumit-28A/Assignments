n = int(input("enter the number: "))
fact = 1
for e in range(n,0,-1):
    fact = fact * e
print("factorial of {}! is :".format(n),fact)