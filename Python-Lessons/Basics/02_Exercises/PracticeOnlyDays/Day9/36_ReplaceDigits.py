# ---Replace all digits with # in a string---

s = input("Enter a string: ")
newString = ""
for i in s:
    if i.isdigit():
        newString += '#'
    else:
        newString += i
print(newString)