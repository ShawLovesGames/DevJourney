# ---Replace digits greater than 5 with #, leave others as is---

s = input("Enter the string: ")
newString = ""
for i in s:
    if i.isdigit():
        if int(i) > 5:
            newString += "#"
        else:
            newString += i
    else:
        newString += i
print(newString)