print("enter your favourite color :")
color = input()
print("i like {} color".format(color))
match color :
    case color if color=="yellow":
        print(color,"-","monday")
    case color if color=="blue":
        print(color,"-","tuesday")
    case color if color=="orange":
        print(color,"-","wednesday")
    case color if color=="white":
        print(color,"-","thursday")
    case color if color=="black":
        print(color,"-","friday")
    case color if color=="red":
        print(color,"-","saturday")
    case color if color=="other":
        print(color,"-","sunday")
