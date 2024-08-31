# ---Replace all spaces with “-” without using .replace()---

s = input("Enter a string: ")
newstring = ""
for i in s:
    if i == " ":
        newstring += '-'
    else:
        newstring += i
print(newstring)