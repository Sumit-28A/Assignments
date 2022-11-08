print("1..triangle is right angled triangle ")
print("2..triangle is isosceles triangle ")
print("3..triangle is equilateral triangle ")
print("enter your choice ")
choice = int(input())
match choice :
    case 1 :
        a,b,c = int(input("enter first number ")),int(input("enter second number ")),int(input("enter third number "))
        if a**2 + b**2 == c**2 :
            print("right angled triangle ")
        else :
            print("not a right angled triangle ")
    case 2 :
        a,b,c = int(input("enter first number ")),int(input("enter second number ")),int(input("enter third number "))
        if a==b or a==c :
            print("triangle is isosceles")
        else:
            print("not isosceles triangle")
    case 3 :
        a,b,c = int(input("enter first number ")),int(input("enter second number ")),int(input("enter third number "))
        if a==b and a==c :
            print("triangle is quilateral triangle ")
        else :
            print("not quilateral triangle ")
    case 4 :
        exit("program is exit")