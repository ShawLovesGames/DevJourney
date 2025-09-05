# ---Replace all non-letters (digits & punctuation) with #---

s = input("Enter the string: ")
newString = ""
for i in s:
    if i.isalpha():
        newString += i
    else:
        newString += '#'
print(newString)