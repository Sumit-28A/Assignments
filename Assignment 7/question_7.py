print("enter the number ")
num = int(input())
match num :
    case num if num>0 :
        print("number is positive ")
    case num if num<0 :
        print("number is negative ")
    case num if num==0 :
        print("number is zero ")