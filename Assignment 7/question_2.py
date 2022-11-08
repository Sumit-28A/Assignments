print("enter 1 for addition","enter 2 for subtraction","enter 3 for multiplication","enter 4 for division",sep="\n") 
num = int(input())
match num :
    case 1 :
        a,b = int(input("enter first number ")), int(input("enter second number "))
        sum = a+b
        print("sum of two numbers ",sum)
    case 2 :
        a,b = int(input("enter first number ")),int(input("enter second number "))
        sub = a-b
        print("subtraction of two number ",sub)
    case 3 :
        a,b = int(input("enter first number ")),int(input("enter the second number "))
        mul = a*b
        print("multiplication of two number ",mul)
    case 4 :
        a,b = int(input("enter first number ")),int(input("enter second number "))
        div = a//b
        print("division of two number ",div)
    case _:
        print("enter correct number ")