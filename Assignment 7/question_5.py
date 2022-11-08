print("enter the number ")
num = int(input())
match num :
    case num if num%2==0 :
        print("Saurabh Shukla Sir ")
    case num if num>0 and num%2 :
        print("Aditya Choudhary Sir ")
    case num if num<0 and num%2:
        print("Prateek Jain Sir ")
    