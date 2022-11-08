print("enter the age")
user_age = int(input())
match user_age :
    case user_age if user_age<10 :
        print("kid")
    case user_age if user_age<20 :
        print("Teen")
    case user_age if user_age<40 :
        print("Young")
    case user_age if user_age<60 :
        print("Experienced")
    case user_age if user_age>=60 and user_age<=100:
        print("Senior Citizen")
    case _:
        print("wrong number")
    