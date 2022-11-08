print("enter a string")
chr = input()
chr.strip()
match chr :
    case chr if " " in chr :
        print("multi word string")
    case chr if " " not in chr :
        print("single word string")