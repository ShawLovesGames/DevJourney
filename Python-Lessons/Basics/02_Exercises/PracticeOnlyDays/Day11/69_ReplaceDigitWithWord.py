# ---Replace Digits with Word---

s = input("Enter a string: ")
newString = ""
for i in s:
    if i.isalpha():
        newString += i
    else:
        if i.isdigit():
            digit = int(i)
            match digit:
                case 1:
                    newString += "one "
                case 2:
                    newString += "two "
                case 3:
                    newString += "three "
                case 4:
                    newString += "four "
                case 5:
                    newString += "five "
                case 6:
                    newString += "six "
                case 7:
                    newString += "seven "
                case 8:
                    newString += "eight "
                case 9:
                    newString += "nine "
                case 0:
                    newString += "zero "
        else:
            newString += i
print(newString)