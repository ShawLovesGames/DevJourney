# ---Keep only the first occurrence of each character---

s = input("Enter the string: ")
newString = ""
for i in s:
    if i == " ":
        newString += i
    elif i not in newString:
        newString += i
print(newString)